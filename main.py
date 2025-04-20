from time import sleep

import aiohttp
import asyncio
import aiofiles
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://www.avito.ru/",
}

ORIGIN = "https://www.avito.ru"

urls = [
    "https://www.avito.ru/tambov/tovary_dlya_kompyutera/dzhoystiki_i_ruli-ASgBAgICAUTGB7ZO?cd=1&q=dualsense+ps5",
]

file = 'avito_ads.txt'

async def fetch(session, url, file_path):
    try:
        async with session.get(url) as response:
            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")
            items = soup.find_all("div", attrs={"data-marker": "item"})
            async with aiofiles.open(file_path, mode='a', encoding='utf-8') as f:
                for item in items:
                    title_tag = item.find('a', attrs={'data-marker': 'item-title'})
                    price_tag = item.find('meta', attrs={'itemprop': 'price'})
                    if title_tag and price_tag:
                        title = title_tag.get('title', '').strip()
                        price = price_tag.get('content', '').strip()
                        href = ORIGIN + title_tag.get('href', '').strip()
                        print(title, price, href)
                        await f.write(f"{title} — {price} ₽ Ссылка: {href}\n\n")
    except Exception as e:
        print(f"Error: {e}")


async def main():
    while True:
        async with aiohttp.ClientSession(headers=headers) as session:
            tasks = [fetch(session, url, file) for url in urls]
            await asyncio.gather(*tasks)
        await asyncio.sleep(30)

asyncio.run(main())
