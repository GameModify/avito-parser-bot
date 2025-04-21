import aiohttp

TELEGRAM_TOKEN = "7657348751:AAHrSXlFwb9l-LaGNjTVTKw6Vr-8uABUqf8"
CHAT_ID = "699235501"

async def send_telegram_message(text: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload) as response:
            if response.status != 200:
                print(f"❌ Ошибка отправки сообщения: {response.status}")
