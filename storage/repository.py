from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.db_models import Ad, SearchQuery


async def get_or_create_search_query(session: AsyncSession, query_text: str) -> SearchQuery:
    res = await session.execute(select(SearchQuery).where(SearchQuery.query == query_text))
    obj = res.scalar_one_or_none()
    if obj:
        return obj
    obj = SearchQuery(query=query_text)
    session.add(obj)
    await session.flush()
    return obj


async def get_ad_by_ad_id(session: AsyncSession, ad_id: str) -> Optional[Ad]:
    res = await session.execute(select(Ad).where(Ad.ad_id == ad_id))
    return res.scalar_one_or_none()


async def upsert_ad(
    session: AsyncSession,
    *,
    ad_id: str,
    title: str,
    price: int,
    url: str,
    search_query: Optional[SearchQuery] = None,
) -> Ad:
    ad = await get_ad_by_ad_id(session, ad_id)
    if ad is None:
        ad = Ad(ad_id=ad_id, title=title, price=price, url=url)
        if search_query:
            ad.search_query = search_query
        session.add(ad)
        await session.flush()
        return ad

    ad.title = title
    ad.price = price
    ad.url = url
    if search_query:
        ad.search_query = search_query
    await session.flush()
    return ad


