import aiofiles
from models import AvitoItem

async def write_items(file_path: str, items: list[AvitoItem]):
    async with aiofiles.open(file_path, mode='a', encoding='utf-8') as f:
        for item in items:
            await f.write(f"{item.title} — {item.price} ₽ Ссылка: {item.url}\n\n")
