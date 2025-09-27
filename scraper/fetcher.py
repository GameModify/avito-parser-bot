from aiocfscrape import CloudflareScraper

async def fetch(session: CloudflareScraper, url: str) -> str:
    async with session.get(url) as response:
        return await response.text()
