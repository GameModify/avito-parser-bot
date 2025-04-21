from asyncio import sleep, run
from aiohttp import ClientSession

from scraper import fetch
from scraper import parse
from scraper import write_items
from config import URLS, HEADERS, FILE_PATH, FETCH_INTERVAL


async def main():
    while True:
        async with ClientSession(headers=HEADERS) as session:
            for url in URLS:
                print('fetching', url)
                html = await fetch(session, url)
                print('parsing HTML')
                items = parse(html)
                print('writing', FILE_PATH)
                await write_items(items, FILE_PATH)
                print(f'Awaiting {FETCH_INTERVAL} seconds')
        await sleep(FETCH_INTERVAL)


if __name__ == "__main__":
    run(main())
