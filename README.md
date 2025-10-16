Avito Parser Bot
================

Quick start
-----------

1. Create virtualenv and install deps:
   ```bash
   python -m venv .venv && .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Copy `.env.example` to `.env` and fill `TELEGRAM_TOKEN`, `CHAT_ID`, `PROXIES` if needed.
3. Run:
   ```bash
   python main.py
   ```

Notes
-----
- Configure `AVITO_URLS` with `page={page}` placeholder.
- Logs of request metrics are written to `metrics.log` and can be summarized with `metrics_report.py`.

