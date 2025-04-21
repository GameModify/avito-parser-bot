from random import randrange
from asyncio import sleep, run
from aiohttp import ClientSession

from config import URLS, HEADERS, FILE_PATH, FETCH_INTERVAL, SEEN_ADS_FILE
from scraper import process_url
from storage.seen_ads import load_seen_ads, save_seen_ads

async def main():
    seen_ads = load_seen_ads(SEEN_ADS_FILE)
    async with ClientSession(headers=HEADERS) as session:
        while True:
            for url in URLS:
                await process_url(
                    session,
                    base_url=url,
                    file_path=FILE_PATH,
                    seen_ads=seen_ads,
                    page_delay=4
                )
            save_seen_ads(seen_ads, SEEN_ADS_FILE)
            await sleep(randrange(FETCH_INTERVAL, FETCH_INTERVAL + 40   ))

if __name__ == "__main__":
    run(main())
