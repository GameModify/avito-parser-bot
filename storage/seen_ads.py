import json
import os
from typing import Set

def load_seen_ads(path: str) -> Set[str]:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return set(json.load(f))
    return set()

def save_seen_ads(seen_ads: Set[str], path: str):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(list(seen_ads), f, ensure_ascii=False, indent=2)
