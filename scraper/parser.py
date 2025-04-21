from bs4 import BeautifulSoup
from models import AvitoItem

def parse(html: str) -> list[AvitoItem]:
    soup = BeautifulSoup(html, "html.parser")
    items = []
    for item_div in soup.find_all("div", attrs={"data-marker": "item"}):
        title_tag = item_div.find('a', attrs={'data-marker': 'item-title'})
        price_tag = item_div.find('meta', attrs={'itemprop': 'price'})
        if title_tag and price_tag:
            title = title_tag.get('title', '').strip()
            price = price_tag.get('content', '').strip()
            href = "https://www.avito.ru" + title_tag.get('href', '').strip()
            items.append(AvitoItem(title, price, href))
    return items
