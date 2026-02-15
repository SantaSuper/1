from pathlib import Path


def test_main_exists() -> None:
    assert Path("app/main.py").exists()


def test_core_files_exist() -> None:
    required = [
        "app/application/use_cases/register_user.py",
        "app/application/use_cases/use_invite_code.py",
        "app/infrastructure/db/sqlite/migrations/001_init.sql",
        "scripts/bootstrap_demo.py",
    ]
    for file_path in required:
        assert Path(file_path).exists(), file_path
