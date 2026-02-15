# RW1 VK Bot (Python)

Готовая стартовая папка с кодом для разработки VK-бота под архитектуру:
- `domain` — сущности и правила;
- `application` — use-case сценарии;
- `infrastructure` — SQLite и репозитории;
- `presentation` — раннер/интерфейс.

## Запуск локально

```bash
python scripts/bootstrap_demo.py
python -m app.main
```

Демо-команды:
- `register`
- `invite` (код `RW1001`)
- `exit`

## Что уже реализовано
- миграции SQLite и базовые таблицы (`users`, `user_levels`, `pending_approvals`, `invite_codes`, `action_logs`);
- use case подачи заявки на регистрацию;
- use case входа по инвайт-коду;
- репозитории для users/pending/invite;
- скрипт `bootstrap_demo.py` для быстрого старта в Colab.

## Тесты

```bash
pytest -q
```
