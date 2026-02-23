Avito Parser Bot
================

STATUS: IN DEVELOPMENT

Quick start
-----------

1. Create virtualenv and install deps:
   ```bash
   python -m venv .venv && .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Copy `.env.example` to `.env` and fill `TELEGRAM_TOKEN`, `CHAT_ID`, `PROXIES` if needed.
3. Initialize DB schema:
   ```bash
   alembic upgrade head
   ```
4. Run:
   ```bash
   python main.py
   ```

Notes
-----
- Configure `AVITO_URLS` with `page={page}` placeholder.
- Logs of request metrics are written to `metrics.log` and can be summarized with `metrics_report.py`.
- JSONL экспорт отключён; данные хранятся в SQLite (`avito.db`).

Database and migrations
-----------------------
- Default DB: SQLite at `./avito.db`. URL can be changed via `DB_URL` in `config.py`.
- Initialize DB schema with Alembic:
  ```bash
  alembic upgrade head
  ```

