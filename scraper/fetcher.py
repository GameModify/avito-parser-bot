import aiohttp
import asyncio
import json
import zstandard as zstd
from config import CAPTCHA_SLEEP_INTERVAL, HEADERS, COOKIES
from utils import send_telegram_message, countdown

MAX_RETRIES = 5
RETRY_DELAY = 10

async def fetch(session: aiohttp.ClientSession, url: str) -> dict:
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            async with session.get(url, headers=HEADERS, cookies=COOKIES) as response:
                encoding = response.headers.get("Content-Encoding", "")

                if response.status in (403, 429):
                    warn_msg = f"⚠️ Блок при запросе {url} (статус {response.status}), попытка {attempt}/{MAX_RETRIES}"
                    print(warn_msg)
                    await countdown(CAPTCHA_SLEEP_INTERVAL * attempt)
                    continue

                raw = await response.read()  # всегда байты

                try:
                    if "application/json" in response.headers.get("Content-Type", "") and not encoding:
                        data = json.loads(raw.decode("utf-8"))
                    elif "zstd" in encoding:
                        dctx = zstd.ZstdDecompressor()
                        with dctx.stream_reader(raw) as reader:
                            decompressed = reader.read()
                        data = json.loads(decompressed.decode("utf-8"))
                    elif "gzip" in encoding or "br" in encoding or "deflate" in encoding:
                        text = await response.text()
                        data = json.loads(text)
                    else:
                        data = json.loads(raw.decode("utf-8"))

                    items = data.get("result", {}).get("items") or data.get("items") or []
                    if not items:
                        print(f"⚠️ На странице {url} объявлений не найдено, попытка {attempt}/{MAX_RETRIES}")
                        await asyncio.sleep(RETRY_DELAY * attempt)
                        continue

                    return data

                except Exception as e:
                    error_msg = f"❌ Ошибка декодирования Avito ответа (encoding={encoding}): {e}"
                    print(error_msg)
                    await asyncio.sleep(RETRY_DELAY * attempt)
                    continue

        except Exception as e:
            error_msg = f"❌ Ошибка при запросе {url}: {e}"
            print(error_msg)
            await asyncio.sleep(RETRY_DELAY * attempt)
            continue

    print(f"❌ Не удалось получить страницу {url} после {MAX_RETRIES} попыток")
    return {}
