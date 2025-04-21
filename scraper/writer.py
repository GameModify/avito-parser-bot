import aiofiles
import json
from typing import List, Dict

async def write_items(items: List[Dict], file_path: str):
    async with aiofiles.open(file_path, mode='a', encoding='utf-8') as f:
        for item in items:
            await f.write(json.dumps(item, ensure_ascii=False) + '\n')
