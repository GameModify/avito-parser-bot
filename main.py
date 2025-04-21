from asyncio import sleep, run
from aiohttp import ClientSession

from config import URLS, HEADERS, FILE_PATH, FETCH_INTERVAL, SEEN_ADS_FILE
from scraper import fetch, get_total_pages, extract_ad_id, parse
from storage import write_items, load_seen_ads, save_seen_ads

seen_ads = load_seen_ads(SEEN_ADS_FILE)

async def process_url(session: ClientSession, base_url: str, file_path: str):
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
                seen_ads.add(ad_id)
                new_items.append(item)
                print(f"🔔 Новое объявление: {item['title']} — {item['price']} ₽\nСсылка: {item['url']}\n")
        await sleep(2)
        await write_items(new_items, file_path)

async def main():
    async with ClientSession(headers=HEADERS) as session:
        while True:
            for url in URLS:
                await process_url(session, url, FILE_PATH)
            save_seen_ads(seen_ads, SEEN_ADS_FILE)
            await sleep(FETCH_INTERVAL)


if __name__ == "__main__":
    run(main())
