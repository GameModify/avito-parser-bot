from random import randrange
from aiohttp import ClientSession
from scraper import fetch, get_total_pages, parse, extract_ad_id
from storage import write_items
from utils import send_telegram_message, countdown


async def process_url(
    session: ClientSession,
    base_url: str,
    file_path: str,
    seen_ads: set,
    page_delay: int = 10
):
    print(f"🌐 Обработка: {base_url}")
    first_html = await fetch(session, base_url)
    total_pages = await get_total_pages(first_html)
    print(f"🔄 Найдено страниц: {total_pages}")

    for page in range(1, total_pages + 1):
        page_url = f"{base_url}&p={page}"
        print(f"📄 Страница {page}/{total_pages} — {page_url}")
        html = await fetch(session, page_url)
        items = await parse(html)

        new_items = []
        for item in items:
            ad_id = await extract_ad_id(item["url"])
            if ad_id not in seen_ads:
                print(f"🔄 новый id: {str(ad_id)}")
                seen_ads.add(ad_id)
                new_items.append(item)
                print(
                    f"🔔 Новое объявление: {item['title']} — "
                    f"{item['price']} ₽\nСсылка: {item['url']}\n"
                )
                msg = (
                    f"🔔 <b>{item['title']}</b>\n"
                    f"💸 Цена: {item['price']} ₽\n"
                    f"🔗 <a href=\"{item['url']}\">Ссылка</a>"
                )
                await send_telegram_message(msg)

        timer = randrange(page_delay, page_delay + 8)
        await countdown(timer)
        await write_items(new_items, file_path)