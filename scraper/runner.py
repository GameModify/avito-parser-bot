from random import randrange
from aiocfscrape import CloudflareScraper
from sqlalchemy.ext.asyncio import AsyncSession
from scraper import fetch, parse, extract_ad_id
from utils import send_telegram_message, countdown
from config import ADDITIONAL_PAGE_FETCH_INTERVAL
from storage.db.session import AsyncSessionLocal
from storage.repository import get_or_create_search_query, upsert_ad, get_ad_by_ad_id



async def process_url(
    session: CloudflareScraper,
    base_url: str,
    page_delay: int
):
    print(f"🌐 Обработка: {base_url}")

    page = 1
    async with AsyncSessionLocal() as db:
        base_for_query = base_url.replace("page={page}", "page=1")
        search_query = await get_or_create_search_query(db, base_for_query)
        while True:
            page_url = base_url.replace("page={page}", f"page={page}")
            print(f"📄 Страница {page} — {page_url}")

            data = await fetch(session, page_url)
            if not data:
                break
            items = await parse(data)

            if not items:
                print(f"✅ На странице {page} объявлений не найдено, остановка.")
                break

            for item in items:
                await handle_new_item_db(db, item, search_query)

            timer = randrange(page_delay, page_delay + ADDITIONAL_PAGE_FETCH_INTERVAL)
            await countdown(timer)

            page += 1

async def handle_new_item_db(db: AsyncSession, item, search_query) -> bool:
    ad_id = await extract_ad_id(item["url"])

    # Check if ad already exists — skip notification if yes
    existing = await get_ad_by_ad_id(db, ad_id)
    if existing:
        await upsert_ad(
            db,
            ad_id=ad_id,
            title=item["title"],
            price=item.get("price", 0),
            url=item["url"],
            search_query=search_query,
        )
        await db.commit()
        return False

    # New ad — insert and notify
    await upsert_ad(
        db,
        ad_id=ad_id,
        title=item["title"],
        price=item.get("price", 0),
        url=item["url"],
        search_query=search_query,
    )
    await db.commit()
    msg = (
        f"🔔 <b>{item['title']}</b>\n"
        f"💸 Цена: {item.get('price', 0)} ₽\n"
        f"🔗 <a href=\"{item['url']}\">Ссылка</a>"
    )
    await send_telegram_message(msg)
    print(f"📢 Новое объявление: {item['title']} — {item.get('price', 0)} ₽")
    return True
