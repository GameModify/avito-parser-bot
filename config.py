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
    "srv_id": "qgBQ0IEmhSLjEJ_-.uExpcQRm4HK2T_yN_wozBLLCCQ9CLckBwgellHxjiKn3xgbqKtu3CgKrvP7G3I4cpBMR.LqYKf4lSnz7nsAPTD3_7DgG7FX_nxdQYm4ZT1f5I2ls=.web",
    "u": "3768jr4x.1fhefk7.1tqegi9zj7j00",
    "uxs_uid": "f552f310-5b2f-11f0-9962-f54972b0033b",
    "__zzatw-avito": "MDA0dBA=Fz2+aQ==",
    "_gcl_au": "1.1.1458558365.1751892201",
    "_ga": "GA1.1.1162737788.1751892202",
    "auth": "1",
    "buyer_laas_location": "656830",
    "buyer_location_id": "656830",
    "_ga_9NLSMYFRV5": "GS2.1.s1758739429$o2$g0$t1758739429$j60$l0$h0",
    "sx": "H4sIAAAAAAAC%2F0zOzUoDMRAA4HeZ8x42M5mZZG8iLNqD%2BIO9Z5KJUJS6CBVb8u6eir7Ax3eBzFgKEXoiUvTce7WgKEXMzD3BcoETLDB%2FNbV1%2Fvy%2B%2Bdkdt%2FMJJnBYgnJGEpE8JqgcS2vUzKJb8%2B6M6tw89cxzcrtS%2FPzo%2B7sVX1%2FWh93%2B%2FfhHBU0acUzQe5RSYxXyolJ78KKWpCMTB490pQ7Zn25t%2B9jkbPfl7fB%2FxTTjGL8BAAD%2F%2F5LprIviAAAA",
    "cfidsw-avito": "qgFRwPbVXeuOUT9X4o2Fte5drF6rFCV6S2KN/dET+fTqa+l8t17hDg9HH9gQpvZckjfz/qPXv+yLJ4RyDSLLy7Ac16FgRL3E3LAwzV8pDmRcP6z+jRSyitQJYyu1detx2DFQv4dQO1TMvegbQoAPR9qvXtjgUgjJxN8wzg==",
    "_ga_ZJDLBTV49B": "GS2.1.s1759429895$o60$g0$t1759429895$j60$l0$h0",
    "v": "1759582535",
    "sessid": "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTk2Njg5MzYsImlhdCI6MTc1OTU4MjUzNiwidSI6MTA4NDIyNDg3LCJwIjo3NTQ0Mjk2NCwicyI6IjdlOWU0NmZjMTY4ZWEyZmQ4ZjZjNWFjM2U4MmU3N2MzLjE3NTk1ODI1MzYiLCJoIjoiZjdhNjgyOGIzMmVkODZlMGQ5YzY5Yjk4ZmNmMWYxNjBfMTc1OTU4MjUzNiIsInYiOm51bGwsImV4dHJhIjpudWxsfQ.Bf0QDaVz6FTuz2h7mp9M9eIUZ98KPFd-VIiKUTbwXe97mEIYQOVGovNgSz0WYQtm1v5eeKaGhYBHpch5Tg0WPQ",
    "rt": "da82c05ade642ca81e511974ae7c0ac0",
    "gMltIuegZN2COuSe": "EOFGWsm50bhh17prLqaIgdir1V0kgrvN",
    "luri": "tambov",
    "ft": "q4+XkFWCRBe+29dTDbyoYVk9tnl0irMrK8WIh7jD69rKQZqhyEsWne8RoU6BEZzkYdqQzlTgOP0XtNWzPBESHAAtmxGXb5HskI0DJ2Pg1lHHouXjQnKUaCfj9wz7uFUqjJnh47z6ryylgD068Rx+jul1a5zwG2O12haaqMDMvuiTHmzkzaGSJebwLpLvA8gf",
    "pageviewCount": "1621",
    "cssid": "cf5716a9-67d4-4c8e-a134-a3903cf20ff5",
    "cssid_exp": "1759584497082",
    "_mlocation": "621540",
    "_mlocation_mode": "default",
    "_adcc": "1.isrJNZ4GS6UYegGdrblfwz00kUQegLXVABN7Bs6hMWF2FqDFHKPog60WwCufpaJkDJG+yu4",
    "csprefid": "c7c4befb-d022-4491-a90b-d897b44a9540"
}

SEEN_ADS_FILE = "seen_ads.json"

TELEGRAM_TOKEN = "7657348751:AAHrSXlFwb9l-LaGNjTVTKw6Vr-8uABUqf8"
CHAT_ID = "699235501"

FETCH_INTERVAL = 180
ADDITIONAL_FETCH_INTERVAL = 8
CAPTCHA_SLEEP_INTERVAL = 60
PAGE_FETCH_INTERVAL = 5
ADDITIONAL_PAGE_FETCH_INTERVAL = 6

TELEGRAM_TIMEOUT = 10  # таймаут запроса в секундах
TELEGRAM_RETRY_COUNT = 3         # количество повторов при ошибке
TELEGRAM_RETRY_DELAY = 5   # задержка между попытками