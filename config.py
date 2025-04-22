ORIGIN = "https://www.avito.ru"

URLS = [
    "https://www.avito.ru/tambov/tovary_dlya_kompyutera/dzhoystiki_i_ruli-ASgBAgICAUTGB7ZO?cd=1&q=dualsense+ps5&s=104",
]

FILE_PATH = 'avito_ads.jsonl'

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://www.avito.ru/",
    "Origin": "https://www.avito.ru",
    "Accept-Language": "ru-RU,ru;q=0.9",
}

COOKIES = {
    "sessid": "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJwIjoyMzY5MjYxNSwidiI6ZmFsc2UsImV4dHJhIjpudWxsLCJleHAiOjE3NDU0MTU5MTIsImlhdCI6MTc0NTMyOTUxMiwicyI6IjQ4MDE1ZDVmZWFiNDRmY2U3MjgzNjhhMjA3NDc4MGJhLjE3NDUzMjk1MTIiLCJoIjoiZTVjNTViMTZmODkxZGZlNDBjZGJhYTg2M2ViYzkzZmZfMTc0NTMyOTUxMiIsInUiOjEzMDUwNDkxNX0.z3ntdwnnYCcq4lmW8ljdiW-WANlY_zmDPCfqemJBYvXIU0-5IGJ8bc_3Rg9-WW-bn7rEp8dfE1zgANJktV58Ig"
}

FETCH_INTERVAL = 180

SEEN_ADS_FILE = 'seen_ads.json'