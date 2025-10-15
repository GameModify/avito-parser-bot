import aiohttp
import asyncio
import json
import zstandard as zstd
from config import CAPTCHA_SLEEP_INTERVAL, HEADERS, COOKIES
from utils import send_telegram_message, countdown


async def fetch(session: aiohttp.ClientSession, url: str) -> dict:
    try:
        async with session.get(url, headers=HEADERS, cookies=COOKIES) as response:
            encoding = response.headers.get("Content-Encoding", "")
            if response.status in (403, 429):
                warn_msg = f"⚠️ Блок при запросе {url} (статус {response.status})"
                print(warn_msg)
                await countdown(CAPTCHA_SLEEP_INTERVAL)
                return {}

            raw = await response.read()  # всегда байты

            if "application/json" in response.headers.get("Content-Type", "") and not encoding:
                return json.loads(raw.decode("utf-8"))

            try:
                if "zstd" in encoding:
                    dctx = zstd.ZstdDecompressor()
                    with dctx.stream_reader(raw) as reader:
                        decompressed = reader.read()
                    return json.loads(decompressed.decode("utf-8"))

                elif "gzip" in encoding or "br" in encoding or "deflate" in encoding:
                    text = await response.text()
                    return json.loads(text)

                else:
                    return json.loads(raw.decode("utf-8"))

            except Exception as e:
                error_msg = f"❌ Ошибка декодирования Avito ответа (encoding={encoding}): {e}"
                print(error_msg)
                return {}

    except Exception as e:
        error_msg = f"❌ Ошибка при запросе {url}: {e}"
        print(error_msg)
        await asyncio.sleep(10)
        return {}
