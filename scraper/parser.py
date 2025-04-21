import re
from typing import List, Dict
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from config import ORIGIN


async def parse(html: str) -> List[Dict]:
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", attrs={"data-marker": "item"})

    results = []
    for item in items:
        title_tag = item.find('a', attrs={'data-marker': 'item-title'})
        price_tag = item.find('meta', attrs={'itemprop': 'price'})

        if title_tag and price_tag:
            results.append({
                "title": title_tag.get('title', '').strip(),
                "price": int(price_tag.get('content', '0').strip()),
                "url": ORIGIN + title_tag.get('href', '').strip()
            })

    return results

async def extract_ad_id(url: str) -> str:
    path = urlparse(url).path  # получаем только путь без параметров
    match = re.search(r'_(\d+)', path)  # ищем _числа
    return match.group(1) if match else url

async def get_total_pages(html: str) -> int:
    soup = BeautifulSoup(html, "html.parser")
    page_buttons = soup.find_all("a", attrs={"data-marker": re.compile(r"pagination-button/page\(\d+\)")})

    page_numbers = []
    for btn in page_buttons:
        match = re.search(r'page\((\d+)\)', btn.get("data-marker", ""))
        if match:
            page_numbers.append(int(match.group(1)))

    return max(page_numbers) if page_numbers else 1
