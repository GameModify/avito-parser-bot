from bs4 import BeautifulSoup
from typing import List, Dict
from config import ORIGIN

def parse(html: str) -> List[Dict]:
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
