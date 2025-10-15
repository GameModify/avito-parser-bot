from random import randrange
from aiocfscrape import CloudflareScraper
from scraper import fetch, parse, extract_ad_id
from storage import write_items, save_seen_ads
from utils import send_telegram_message, countdown
from config import SEEN_ADS_FILE, ADDITIONAL_PAGE_FETCH_INTERVAL


async def process_url(
    session: CloudflareScraper,
    base_url: str,
    file_path: str,
    seen_ads: set,
    page_delay: int
):
    print(f"🌐 Обработка: {base_url}")

    page = 1
    while True:
        page_url = base_url.replace("page={page}", f"page={page}")
        print(f"📄 Страница {page} — {page_url}")

        data = await fetch(session, page_url)
        items = await parse(data)

        if not items:
            print(f"✅ На странице {page} объявлений не найдено, остановка.")
            break

        new_items = []
        for item in items:
            if await handle_new_item(item, seen_ads, SEEN_ADS_FILE):
                new_items.append(item)

        await write_items(new_items, file_path)

        timer = randrange(page_delay, page_delay + ADDITIONAL_PAGE_FETCH_INTERVAL)
        await countdown(timer)

        page += 1

async def handle_new_item(item, seen_ads, seen_ads_file):
    ad_id = await extract_ad_id(item["url"])
    if ad_id in seen_ads:
        return False
    seen_ads.add(ad_id)
    await save_seen_ads(seen_ads, seen_ads_file)
    msg = (
        f"🔔 <b>{item['title']}</b>\n"
        f"💸 Цена: {item['price']} ₽\n"
        f"🔗 <a href=\"{item['url']}\">Ссылка</a>"
    )
    await send_telegram_message(msg)
    print(f"📢 Новое объявление: {item['title']} — {item['price']} ₽")
    return True
