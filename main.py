from random import randrange
from asyncio import run
from storage.seen_ads import load_seen_ads
from scraper.session import create_session
from scraper.runner import process_url
from utils import countdown
from config import URLS, FILE_PATH, FETCH_INTERVAL, SEEN_ADS_FILE, PAGE_FETCH_INTERVAL


async def main():
    seen_ads = await load_seen_ads(SEEN_ADS_FILE)
    session = await create_session()

    try:
        while True:
            for url in URLS:
                await process_url(
                    session=session,
                    base_url=url,
                    file_path=FILE_PATH,
                    seen_ads=seen_ads,
                    page_delay=PAGE_FETCH_INTERVAL
                )

            timer = randrange(FETCH_INTERVAL, FETCH_INTERVAL + 40)
            await countdown(timer)

    finally:
        await session.close()


if __name__ == "__main__":
    run(main())
