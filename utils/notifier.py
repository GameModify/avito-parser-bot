import aiohttp
import asyncio

from config import TELEGRAM_TOKEN, CHAT_ID, TELEGRAM_RETRY_COUNT, TELEGRAM_RETRY_DELAY, TELEGRAM_TIMEOUT


async def send_telegram_message(text: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }

    for attempt in range(1, TELEGRAM_RETRY_COUNT + 1):
        try:
            async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=TELEGRAM_TIMEOUT)) as session:
                async with session.post(url, data=payload) as response:
                    if response.status == 200:
                        return
                    else:
                        print(f"❌ Попытка {attempt}: ошибка отправки сообщения (HTTP {response.status})")
        except aiohttp.ClientError as e:
            print(f"❌ Попытка {attempt}: ошибка соединения с Telegram: {e}")
        except asyncio.TimeoutError:
            print(f"❌ Попытка {attempt}: таймаут при отправке сообщения")

        if attempt < TELEGRAM_RETRY_COUNT:
            await asyncio.sleep(TELEGRAM_RETRY_DELAY)

    print("⚠️ Не удалось отправить сообщение после нескольких попыток")
