import json
import aiofiles


async def load_seen_ads(file_path: str) -> set:
    try:
        async with aiofiles.open(file_path, "r", encoding="utf-8") as f:
            data = await f.read()
            return set(json.loads(data))
    except FileNotFoundError:
        return set()
    except json.JSONDecodeError:
        return set()


async def save_seen_ads(seen_ads: set, file_path: str):
    async with aiofiles.open(file_path, "w", encoding="utf-8") as f:
        formatted = json.dumps(list(seen_ads), indent=2, ensure_ascii=False)
        await f.write(formatted)