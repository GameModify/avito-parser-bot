

SEEN_ADS_FILE = "seen_ads.json"

TELEGRAM_TOKEN = "TELEGRAM_TOKEN_HERE"
CHAT_ID = "YOU'RE CHAT ID"

FETCH_INTERVAL = 180
ADDITIONAL_FETCH_INTERVAL = 12
CAPTCHA_SLEEP_INTERVAL = 60
PAGE_FETCH_INTERVAL = 25
ADDITIONAL_PAGE_FETCH_INTERVAL = 12

TELEGRAM_TIMEOUT = 10
TELEGRAM_RETRY_COUNT = 3
TELEGRAM_RETRY_DELAY = 5

USE_PROXY = True

PROXIES = [
    "socks5://LOGIN:PASS@IP:PORT",
]



ORIGIN = "https://m.avito.ru"

URLS = [
    "https://m.avito.ru/api/11/items?"
    "key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&"
    "query=dualsense+ps5&locationId=656830&page={page}&presentationType=serp"
]

FILE_PATH = "avito_ads.jsonl"

HEADERS = {
    ":authority": "m.avito.ru",
    ":method": "GET",
    ":path": "/api/11/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&query=dualsense+ps5&locationId=656830&page=1&presentationType=serp",
    ":scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "priority": "u=0, i",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (iPad; CPU OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1",
}

COOKIES = {
    YOURE COOKIES
}


# Database (SQLite URL for SQLAlchemy async engine)
DB_URL = "sqlite+aiosqlite:///./avito.db"
