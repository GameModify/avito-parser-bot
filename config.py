ORIGIN = "https://www.avito.ru"

URLS = [
    "https://www.avito.ru/tambov/tovary_dlya_kompyutera/dzhoystiki_i_ruli-ASgBAgICAUTGB7ZO?cd=1&q=dualsense+ps5&s=104",
]

FILE_PATH = 'avito_ads.jsonl'

HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "ru-RU,ru;q=0.9",
    "cache-control": "max-age=0",
    "priority": "u=0, i",
    "sec-ch-ua": '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Mobile Safari/537.36",
    "referer": "https://www.avito.ru/",
}

COOKIES = {
    "sessid": "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJwIjoyMzY5MjYxNSwidiI6ZmFsc2UsImV4dHJhIjpudWxsLCJleHAiOjE3NDU0MTU5MTIsImlhdCI6MTc0NTMyOTUxMiwicyI6IjQ4MDE1ZDVmZWFiNDRmY2U3MjgzNjhhMjA3NDc4MGJhLjE3NDUzMjk1MTIiLCJoIjoiZTVjNTViMTZmODkxZGZlNDBjZGJhYTg2M2ViYzkzZmZfMTc0NTMyOTUxMiIsInUiOjEzMDUwNDkxNX0.z3ntdwnnYCcq4lmW8ljdiW-WANlY_zmDPCfqemJBYvXIU0-5IGJ8bc_3Rg9-WW-bn7rEp8dfE1zgANJktV58Ig"
}

SEEN_ADS_FILE = 'seen_ads.json'

FETCH_INTERVAL = 180
ADDITIONAL_FETCH_INTERVAL = 8
CAPTCHA_SLEEP_INTERVAL = 60
PAGE_FETCH_INTERVAL = 4
ADDITIONAL_PAGE_FETCH_INTERVAL = 4
