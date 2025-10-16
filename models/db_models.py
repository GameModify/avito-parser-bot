from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from storage.db.base import Base


class SearchQuery(Base):
    __tablename__ = "search_queries"

    id = Column(Integer, primary_key=True)
    query = Column(Text, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    ads = relationship("Ad", back_populates="search_query")


class Ad(Base):
    __tablename__ = "ads"

    id = Column(Integer, primary_key=True)
    ad_id = Column(String(64), nullable=False)
    title = Column(Text, nullable=False)
    price = Column(Integer, default=0, nullable=False)
    url = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    search_query_id = Column(Integer, ForeignKey("search_queries.id"), nullable=True)
    search_query = relationship("SearchQuery", back_populates="ads")

    __table_args__ = (
        UniqueConstraint("ad_id", name="uq_ads_ad_id"),
    )


