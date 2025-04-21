from asyncio import sleep, run
from aiohttp import ClientSession

from config import URLS, HEADERS, FILE_PATH, FETCH_INTERVAL
from scraper import fetch, get_total_pages
from scraper import parse
from scraper import write_items

async def process_url(session: ClientSession, base_url: str, file_path: str):
    print(f"🌐 Обработка: {base_url}")
    first_html = await fetch(session, base_url)
    total_pages = get_total_pages(first_html)

    print(f"🔄 Найдено страниц: {total_pages}")

    for page in range(1, total_pages + 1):
        page_url = f"{base_url}&p={page}"
        print(f"📄 Страница {page}/{total_pages} — {page_url}")
        html = await fetch(session, page_url)
        items = parse(html)
        await write_items(items, file_path)

async def main():
    async with ClientSession(headers=HEADERS) as session:
        for url in URLS:
            await process_url(session, url, FILE_PATH)
            await sleep(FETCH_INTERVAL)


if __name__ == "__main__":
    run(main())
