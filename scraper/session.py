import random
import asyncio
from aiocfscrape import CloudflareScraper
from utils import get_request_headers, get_request_cookies
from config import HEADERS, COOKIES, PROXIES, USE_PROXY
from aiohttp_socks import ProxyConnector

from utils import get_ip_via_proxy, get_ip_via_proxy_direct

MAX_RETRIES = 5


async def create_session() -> CloudflareScraper:
    proxy = random.choice(PROXIES) if (USE_PROXY and PROXIES) else None
    if proxy:
        connector = ProxyConnector.from_url(proxy)
        print(f"🌐 Используется прокси: {proxy}")
        await get_ip_via_proxy(proxy)
    else:
        connector = None
        print("🚀 Прокси отключен, работа напрямую")
        await get_ip_via_proxy_direct()

    session = CloudflareScraper(
        headers=get_request_headers(HEADERS),
        cookies=get_request_cookies(COOKIES),
        connector=connector
    )

    session._proxy_url = proxy
    return session

async def fetch_with_retry(session: CloudflareScraper, url: str) -> dict:
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = await session.get(url)
            if response.status == 200:
                return await response.json()

            if response.status in {403, 429}:
                print(f"⚠️ [{response.status}] Доступ ограничен. Переинициализация сессии...")
                await asyncio.sleep(random.randint(5, 15))

                await session.close()
                session = await create_session()
                continue

            print(f"⚠️ Неожиданный статус {response.status} при попытке {attempt}/{MAX_RETRIES}")
            await asyncio.sleep(3)
        except Exception as e:
            print(f"❌ Ошибка при запросе ({attempt}/{MAX_RETRIES}): {e}")
            await asyncio.sleep(3)

    raise RuntimeError(f"Не удалось получить ответ с {url} после {MAX_RETRIES} попыток.")
