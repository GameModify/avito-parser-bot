# parser.py
import re
import json
from typing import List, Dict, Any
from urllib.parse import urlparse

from config import ORIGIN


def _parse_price_field(p: Any) -> int:
    """
    Попытаться извлечь целочисленную цену из разных форматов:
    - int / float -> int
    - str -> оставить только цифры (учитывает пробелы, неразрывные пробелы и т.п.)
    - dict -> ищем по ключам: value, amount, current, price, raw, display, text и т.д.
    Возвращает 0 если не удалось распарсить.
    """
    if p is None:
        return 0

    # Число
    if isinstance(p, (int, float)):
        try:
            return int(p)
        except Exception:
            return 0

    # Строка — убираем все нецифровые символы, затем собираем число
    if isinstance(p, str):
        # заменим неразрывные пробелы и т.п.
        s = p.replace('\u00A0', ' ').strip()
        # извлечь все группы цифр и склеить (1 250 -> 1250, "250 ₽" -> 250)
        groups = re.findall(r'\d+', s)
        if not groups:
            return 0
        try:
            return int(''.join(groups))
        except Exception:
            return 0

    # Словарь — пробуем стандартные ключи и рекурсивно
    if isinstance(p, dict):
        # порядок важен — пробуем наиболее вероятные ключи
        for key in ("value", "amount", "current", "price", "raw", "display", "text"):
            if key in p and p[key] is not None and p[key] != "":
                v = _parse_price_field(p[key])
                if v:
                    return v

        # иногда value сам по себе — вложенный объект
        if "value" in p and isinstance(p["value"], dict):
            v = _parse_price_field(p["value"])
            if v:
                return v

        # fallback: попытаться найти первые цифры в сериализованном виде
        try:
            s = json.dumps(p, ensure_ascii=False)
            groups = re.findall(r'\d+', s)
            if groups:
                return int(''.join(groups))
        except Exception:
            pass

    # Неизвестный формат
    return 0


async def parse(data: dict) -> List[Dict]:
    """
    Парсинг JSON ответа Avito API — возвращает список объектов:
    {"title": ..., "price": int_price, "url": ...}
    """
    results: List[Dict] = []

    items = []
    if isinstance(data, dict):
        items = data.get("result", {}).get("items") or data.get("items") or []
    if not items and isinstance(data, list):
        items = data

    for obj in items:
        if not isinstance(obj, dict):
            continue

        if obj.get("type") and obj.get("type") != "item":
            continue

        value = obj.get("value", obj)  # если объект уже value-like


        title = value.get("title") or value.get("name") or ""
        title = title.strip() if isinstance(title, str) else ""


        uri = value.get("uri") or value.get("url") or value.get("link") or ""
        url = ORIGIN + uri if uri else ""


        price_field = value.get("price") or value.get("priceInfo") or value.get("price_data") or None
        price = _parse_price_field(price_field)

        if price == 0 and price_field:
            try:
                pf_preview = (
                    price_field if isinstance(price_field, str)
                    else json.dumps(price_field, ensure_ascii=False)[:200]
                )
            except Exception:
                pf_preview = str(price_field)[:200]
            print(f"⚠️ Не распознана цена, raw price_field: {pf_preview}")


        if not title or not url:
            continue

        results.append({
            "title": title,
            "price": price,
            "url": url
        })

    return results


async def extract_ad_id(url: str) -> str:
    """
    Берёт id объявления из пути URL — возвращает последнюю группу цифр в пути.
    Пример: /.../название_7217746735 -> 7217746735
    """
    path = urlparse(url).path  # только путь без параметров
    matches = re.findall(r'(\d+)', path)
    return matches[-1] if matches else url


async def get_total_pages(data: dict) -> int:
    """
    Ищем количество страниц в JSON-ответе Avito.
    """
    if not isinstance(data, dict):
        return 1

    # пробуем стандартные места
    meta = (
        data.get("result", {}).get("pagination")
        or data.get("pagination")
        or data.get("pager")
        or {}
    )

    # пробуем разные ключи
    for key in ("pages", "totalPages", "total_pages", "total"):
        if key in meta and meta[key]:
            try:
                return int(meta[key])
            except Exception:
                continue

    # если ничего не нашли, пробуем по числу объявлений
    try:
        total_count = meta.get("totalCount") or meta.get("total_count")
        per_page = meta.get("perPage") or meta.get("per_page") or 50
        if total_count:
            return (int(total_count) + int(per_page) - 1) // int(per_page)
    except Exception:
        pass

    return 1

