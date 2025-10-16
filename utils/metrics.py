import json
from typing import Optional

_METRICS_FILE = "metrics.log"

async def log_metric(
    url: str,
    status: int,
    success: bool,
    proxy: Optional[str] = None,
    headers: Optional[dict] = None,
    cookies: Optional[dict] = None,
    error: Optional[str] = None
):
    """
    Логируем метрику запроса.
    """
    entry = {
        "url": url,
        "status": status,
        "success": success,
        "proxy": proxy,
        "headers": headers,
        "cookies": cookies,
        "error": error
    }


    with open(_METRICS_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
