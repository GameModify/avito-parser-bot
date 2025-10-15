from random import randrange
from asyncio import run
from aiocfscrape import CloudflareScraper

from config import URLS, HEADERS, COOKIES, FILE_PATH, FETCH_INTERVAL, SEEN_ADS_FILE, PAGE_FETCH_INTERVAL
from scraper import process_url
from storage.seen_ads import load_seen_ads
from utils import countdown, get_request_cookies, get_request_headers


async def main():
    seen_ads = await load_seen_ads(SEEN_ADS_FILE)
    async with CloudflareScraper(headers=get_request_headers(HEADERS), cookies=get_request_cookies(COOKIES)) as session:
        while True:
            for url in URLS:
                await process_url(
                    session,
                    base_url=url,
                    file_path=FILE_PATH,
                    seen_ads=seen_ads,
                    page_delay=PAGE_FETCH_INTERVAL
                )
            timer = randrange(FETCH_INTERVAL, FETCH_INTERVAL + 40  )
            await countdown(timer)


if __name__ == "__main__":
    run(main())
