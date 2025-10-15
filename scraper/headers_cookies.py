import random
import time
import uuid
import base64
import zlib
from typing import Dict, Any

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15",
    "Mozilla/5.0 (iPad; CPU OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Mobile Safari/537.36",
]

ACCEPTS = [
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "application/json, text/plain, */*",
]

ACCEPT_LANGS = [
    "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "en-US,en;q=0.9,ru;q=0.8",
]

SEC_FETCH_SITE = ["none", "same-origin", "same-site"]

def _make_random_pageviewcount() -> str:
    return str(random.randint(1000, 999999))

def _make_cssid() -> str:
    return str(uuid.uuid4())

def _make_luri_from_region(region: str = "tambov") -> str:
    return region

def _make_sx_token() -> str:
    # sx у тебя — это похоже на base64/gzipped payload; мы можем сгенерировать
    # безопасный псевдо-token: base64(zlib(uuid()))
    payload = uuid.uuid4().hex.encode("utf-8")
    gz = zlib.compress(payload)
    return base64.urlsafe_b64encode(gz).decode("ascii").rstrip("=")

def get_request_headers(base_headers: Dict[str, Any]) -> Dict[str, str]:
    """
    Возвращает клон HEADERS с ротацией некоторых полей.
    Не меняем :path/:method/:scheme — они для HTTP/2, но можно оставить.
    """
    headers = dict(base_headers or {})

    headers["user-agent"] = random.choice(USER_AGENTS)

    headers["accept"] = random.choice(ACCEPTS)
    headers["accept-language"] = random.choice(ACCEPT_LANGS)

    headers["sec-fetch-site"] = random.choice(SEC_FETCH_SITE)
    headers["sec-fetch-mode"] = "navigate"
    headers["sec-fetch-dest"] = "document"

    for k in list(headers.keys()):
        if k.startswith(":"):
            continue

    return headers

def get_request_cookies(base_cookies: Dict[str, str], region: str = "moskva") -> Dict[str, str]:
    """
    Возвращает модифицированную копию COOKIES:
    - не трогаем важные аутентификационные ключи (если их нет — оставь как есть)
    - ротация только неблокирующих cookie-полей
    """
    cookies = dict(base_cookies or {})

    safe_keys = [
        "pageviewCount", "cssid", "cssid_exp", "v", "luri", "_mlocation",
        "sx", "rt", "ft"
    ]

    if "pageviewCount" in cookies or True:
        cookies["pageviewCount"] = _make_random_pageviewcount()

    cookies["cssid"] = _make_cssid()
    cookies["cssid_exp"] = str(int(time.time()) + 60 * 60)  # час вперёд
    cookies["v"] = str(int(time.time()))
    cookies["luri"] = _make_luri_from_region(region)

    cookies["sx"] = _make_sx_token()

    return cookies
