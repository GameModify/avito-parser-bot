import json
from collections import Counter, defaultdict
import os

METRICS_FILE = "metrics.log"

if not os.path.exists(METRICS_FILE):
    print(f"❌ Файл {METRICS_FILE} не найден.")
    exit(1)

success_count = 0
fail_count = 0
proxy_counter = Counter()
user_agent_counter = Counter()
errors = []

with open(METRICS_FILE, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            data = json.loads(line)
        except Exception as e:
            print(f"⚠️ Ошибка при разборе строки: {e}")
            continue

        if data.get("success"):
            success_count += 1
        else:
            fail_count += 1
            errors.append({
                "url": data.get("url"),
                "status": data.get("status"),
                "error": data.get("error")
            })

        proxy_counter[data.get("proxy")] += 1

        headers = data.get("headers") or {}
        ua = headers.get("user-agent")
        if ua:
            user_agent_counter[ua] += 1

# 📊 Отчёт
print("=== METRICS REPORT ===")
print(f"✅ Успешных запросов: {success_count}")
print(f"❌ Ошибочных запросов: {fail_count}")
print("\n🌐 Используемые прокси (кол-во запросов):")
for proxy, count in proxy_counter.most_common():
    print(f"  {proxy}: {count}")

print("\n🖥 Топ User-Agent:")
for ua, count in user_agent_counter.most_common(5):
    print(f"  {ua}: {count}")

if errors:
    print("\n❌ Список ошибок:")
    for e in errors:
        print(f"  [{e['status']}] {e['url']} -> {e['error']}")
else:
    print("\nВсе запросы прошли успешно! 🎉")
