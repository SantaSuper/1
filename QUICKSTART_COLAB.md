# Быстрый старт в Google Colab

```bash
!git clone <YOUR_REPO_URL> rw1_vk_bot
%cd rw1_vk_bot
!pip install -r requirements.txt
!python scripts/bootstrap_demo.py
!python -m app.main
```

Команды в локальном раннере:
- `register` — создать заявку на регистрацию;
- `invite` — вход по коду (демо-код `RW1001`);
- `exit` — выход.
