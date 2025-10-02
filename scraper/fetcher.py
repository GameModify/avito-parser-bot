import aiohttp

from config import CAPTCHA_SLEEP_INTERVAL
from utils import send_telegram_message, countdown
import asyncio


async def fetch(session: aiohttp.ClientSession, url: str) -> str:
    try:
        async with session.get(url) as response:
            text = await response.text()

            if "captcha" in text.lower() or response.status in (403, 429):
                warn_msg = (
                    f"⚠️ Обнаружена капча при запросе {url}\n"
                    f"Статус: {response.status}"
                )
                print(warn_msg)
                await countdown(CAPTCHA_SLEEP_INTERVAL)
                return ""

            return text

    except Exception as e:
        error_msg = f"❌ Ошибка при запросе {url}: {e}"
        print(error_msg)
        await send_telegram_message(error_msg)
        await asyncio.sleep(10)
        return ""