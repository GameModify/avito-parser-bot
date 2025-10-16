from random import randrange
from asyncio import run
from scraper.session import create_session
from scraper.runner import process_url
from utils import countdown
from config import URLS, FETCH_INTERVAL, PAGE_FETCH_INTERVAL


async def main():
    session = await create_session()

    try:
        while True:
            for url in URLS:
                await process_url(
                    session=session,
                    base_url=url,
                    page_delay=PAGE_FETCH_INTERVAL
                )

            timer = randrange(FETCH_INTERVAL, FETCH_INTERVAL + 40)
            await countdown(timer)

    finally:
        await session.close()


if __name__ == "__main__":
    run(main())
