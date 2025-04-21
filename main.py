import asyncio
import aiohttp
from scraper import fetch
from scraper import parse
from scraper import write_items
from config import URLS, HEADERS, FILE_PATH

async def main():
    while True:
        async with aiohttp.ClientSession(headers=HEADERS) as session:
            for url in URLS:
                print('fetching', url)
                html = await fetch(session, url)
                print('parsing HTML')
                items = parse(html)
                print('writing', FILE_PATH)
                await write_items(FILE_PATH, items)
                print(f'Awaiting 30 seconds')
        await asyncio.sleep(30)

if __name__ == "__main__":
    asyncio.run(main())
