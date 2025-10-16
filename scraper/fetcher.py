import aiohttp
import asyncio
import json
import zstandard as zstd
import random
from typing import Dict
from config import HEADERS, COOKIES, USE_PROXY
from scraper.session import create_session
from utils import countdown, get_request_headers, get_request_cookies, log_metric

MAX_RETRIES = 6
BASE_RETRY_DELAY = 5  # сек
MAX_BACKOFF = 300
JITTER = 0.25


def _apply_jitter(delay: float) -> float:
    jitter = delay * JITTER
    return max(0.0, delay + random.uniform(-jitter, jitter))

async def _wait_retry(response: aiohttp.ClientResponse, attempt: int):
    ra = response.headers.get("Retry-After")
    try:
        ra_val = int(ra) if ra else None
    except Exception:
        ra_val = None

    if ra_val:
        wait = ra_val + random.uniform(1, 3)
    else:
        wait = min(BASE_RETRY_DELAY * (2 ** (attempt - 1)), MAX_BACKOFF)

    await countdown(int(_apply_jitter(wait)))

async def _simple_backoff(attempt: int):
    delay = min(BASE_RETRY_DELAY * (2 ** (attempt - 1)), MAX_BACKOFF)
    await countdown(int(_apply_jitter(delay)))

async def fetch(session: aiohttp.ClientSession, url: str) -> Dict:
    proxy_used = getattr(session, "_proxy_url", None)
    for attempt in range(1, MAX_RETRIES + 1):
        headers = get_request_headers(HEADERS)
        cookies = get_request_cookies(COOKIES)
        try:
            timeout = aiohttp.ClientTimeout(total=30)

            async with session.get(url, headers=headers, cookies=cookies, timeout=timeout) as response:
                status = response.status
                encoding = response.headers.get("Content-Encoding", "")

                if status in (403, 429):
                    await log_metric(url, status, False, proxy_used, headers, cookies, error=f"Blocked with {status}")
                    print(f"⚠️ Блок при запросе {url} (статус {status}), попытка {attempt}/{MAX_RETRIES}")
                    if USE_PROXY:
                        try:
                            print("🔁 Пересоздаю сессию с новым proxy/headers/cookies...")
                            await session.close()
                            session = await create_session()
                        except Exception as e:
                            print(f"⚠️ Ошибка пересоздания сессии: {e}")
                    await _wait_retry(response, attempt)
                    continue

                raw = await response.read()
                try:
                    content_type = response.headers.get("Content-Type", "")
                    if "zstd" in encoding:
                        dctx = zstd.ZstdDecompressor()
                        with dctx.stream_reader(raw) as reader:
                            decompressed = reader.read()
                        data = json.loads(decompressed.decode("utf-8"))
                    elif "application/json" in content_type and not encoding:
                        data = json.loads(raw.decode("utf-8"))
                    else:
                        text = await response.text()
                        data = json.loads(text)
                except Exception as e:
                    await log_metric(url, status, False, proxy_used, headers, cookies, error=str(e))
                    print(f"❌ Ошибка декодирования ответа (attempt {attempt}): {e}")
                    delay = min(BASE_RETRY_DELAY * (2 ** (attempt - 1)), MAX_BACKOFF)
                    await countdown(_apply_jitter(delay))
                    continue


                await log_metric(url, status, True, proxy_used, headers, cookies)
                return data

        except asyncio.TimeoutError:
            await log_metric(url, 0, False, proxy_used, headers, cookies, error="Timeout")
            print(f"❌ Timeout при запросе {url} (attempt {attempt}/{MAX_RETRIES})")
        except aiohttp.ClientError as e:
            await log_metric(url, 0, False, proxy_used, headers, cookies, error=str(e))
            print(f"❌ ClientError при запросе {url} (attempt {attempt}/{MAX_RETRIES}): {e}")
        except Exception as e:
            await log_metric(url, 0, False, proxy_used, headers, cookies, error=str(e))
            print(f"❌ Ошибка при запросе {url} (attempt {attempt}/{MAX_RETRIES}): {e}")

        delay = min(BASE_RETRY_DELAY * (2 ** (attempt - 1)), MAX_BACKOFF)
        await countdown(_apply_jitter(delay))

    await log_metric(url, 0, False, proxy_used, headers, cookies, error="Max retries exceeded")
    print(f"❌ Не удалось получить страницу {url} после {MAX_RETRIES} попыток")
    return {}
