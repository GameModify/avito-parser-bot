from asyncio import sleep


async def countdown(seconds: int or float):
    print(f"🔧 Ожидаю {seconds} секунд.")
    for i in range(int(seconds), 0, -1):
        print(f"\r⏳ Ждём {i} секунд...", end="", flush=True)
        await sleep(1)
    print("\r✅ Продолжаем!")