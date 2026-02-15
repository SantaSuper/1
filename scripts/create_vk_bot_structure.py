#!/usr/bin/env python3
"""Create a starter folder architecture for the RW1 VK bot project.

Usage (local):
    python scripts/create_vk_bot_structure.py

Usage (Google Colab):
    !python scripts/create_vk_bot_structure.py --root /content/rw1_vk_bot
"""

from __future__ import annotations

import argparse
from pathlib import Path
from textwrap import dedent

FILES: dict[str, str] = {
    "app/__init__.py": "",
    "app/main.py": dedent(
        '''\
        """Application entrypoint."""

        from app.presentation.vk.runner import start_polling


        if __name__ == "__main__":
            start_polling()
        '''
    ),
    "app/config.py": dedent(
        '''\
        """Centralized configuration for the bot."""

        from dataclasses import dataclass
        import os


        @dataclass(slots=True)
        class Settings:
            vk_group_token: str
            vk_group_id: int
            sqlite_path: str = "data/rw1.db"


        def load_settings() -> Settings:
            return Settings(
                vk_group_token=os.getenv("VK_GROUP_TOKEN", ""),
                vk_group_id=int(os.getenv("VK_GROUP_ID", "0")),
                sqlite_path=os.getenv("SQLITE_PATH", "data/rw1.db"),
            )
        '''
    ),
    "app/domain/__init__.py": "",
    "app/domain/entities/__init__.py": "",
    "app/domain/entities/user.py": dedent(
        '''\
        """Domain entity: user."""

        from dataclasses import dataclass


        @dataclass(slots=True)
        class User:
            vk_id: int
            nickname: str
            faction: str | None = None
            position: str | None = None
            rp_name: str | None = None
            registered: bool = False
        '''
    ),
    "app/domain/entities/faction.py": dedent(
        '''\
        """Domain constants for factions."""

        FACTIONS = ("Армия", "МВД", "СМИ", "Политика", "ФСБ", "Больница")
        '''
    ),
    "app/domain/services/__init__.py": "",
    "app/application/__init__.py": "",
    "app/application/use_cases/__init__.py": "",
    "app/application/use_cases/register_user.py": dedent(
        '''\
        """Use case placeholder for registration flow."""

        from app.domain.entities.user import User


        def build_registration_request(vk_id: int, nickname: str) -> User:
            return User(vk_id=vk_id, nickname=nickname, registered=False)
        '''
    ),
    "app/infrastructure/__init__.py": "",
    "app/infrastructure/db/__init__.py": "",
    "app/infrastructure/db/sqlite/__init__.py": "",
    "app/infrastructure/db/sqlite/connection.py": dedent(
        '''\
        """SQLite connection helpers."""

        import sqlite3
        from pathlib import Path


        def get_connection(db_path: str) -> sqlite3.Connection:
            Path(db_path).parent.mkdir(parents=True, exist_ok=True)
            conn = sqlite3.connect(db_path)
            conn.row_factory = sqlite3.Row
            return conn
        '''
    ),
    "app/infrastructure/db/sqlite/migrations/001_init.sql": dedent(
        '''\
        -- Initial schema placeholder
        CREATE TABLE IF NOT EXISTS users (
            vk_id INTEGER PRIMARY KEY,
            nickname TEXT NOT NULL,
            faction TEXT,
            position TEXT,
            rp_name TEXT,
            registered INTEGER NOT NULL DEFAULT 0,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        '''
    ),
    "app/infrastructure/repositories/__init__.py": "",
    "app/infrastructure/repositories/user_repository.py": dedent(
        '''\
        """Repository placeholder for user persistence."""

        from app.domain.entities.user import User
        from app.infrastructure.db.sqlite.connection import get_connection


        class UserRepository:
            def __init__(self, db_path: str) -> None:
                self._db_path = db_path

            def save(self, user: User) -> None:
                with get_connection(self._db_path) as conn:
                    conn.execute(
                        """
                        INSERT INTO users(vk_id, nickname, faction, position, rp_name, registered)
                        VALUES(?, ?, ?, ?, ?, ?)
                        ON CONFLICT(vk_id) DO UPDATE SET
                            nickname=excluded.nickname,
                            faction=excluded.faction,
                            position=excluded.position,
                            rp_name=excluded.rp_name,
                            registered=excluded.registered
                        """,
                        (
                            user.vk_id,
                            user.nickname,
                            user.faction,
                            user.position,
                            user.rp_name,
                            int(user.registered),
                        ),
                    )
        '''
    ),
    "app/presentation/__init__.py": "",
    "app/presentation/vk/__init__.py": "",
    "app/presentation/vk/runner.py": dedent(
        '''\
        """VK runner placeholder.

        Replace with vk_api / vkbottle startup logic.
        """


        def start_polling() -> None:
            print("VK bot skeleton is ready. Connect your VK SDK here.")
        '''
    ),
    "app/presentation/vk/handlers/__init__.py": "",
    "app/presentation/vk/keyboards/__init__.py": "",
    "app/presentation/vk/states/__init__.py": "",
    "tests/__init__.py": "",
    "tests/test_structure_smoke.py": dedent(
        '''\
        from pathlib import Path


        def test_main_exists() -> None:
            assert Path("app/main.py").exists()
        '''
    ),
    "data/.gitkeep": "",
    ".env.example": dedent(
        '''\
        VK_GROUP_TOKEN=
        VK_GROUP_ID=0
        SQLITE_PATH=data/rw1.db
        '''
    ),
    "requirements.txt": dedent(
        '''\
        pytest>=8.0.0
        '''
    ),
}

DIRECTORIES = [
    "app",
    "app/domain/entities",
    "app/domain/services",
    "app/application/use_cases",
    "app/infrastructure/db/sqlite/migrations",
    "app/infrastructure/repositories",
    "app/presentation/vk/handlers",
    "app/presentation/vk/keyboards",
    "app/presentation/vk/states",
    "tests",
    "data",
    "scripts",
]


def create_structure(root: Path, overwrite: bool) -> None:
    for directory in DIRECTORIES:
        (root / directory).mkdir(parents=True, exist_ok=True)

    for relative, content in FILES.items():
        file_path = root / relative
        if file_path.exists() and not overwrite:
            continue
        file_path.write_text(content, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create RW1 VK bot folder architecture")
    parser.add_argument("--root", default=".", help="Project root path")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = Path(args.root).resolve()
    root.mkdir(parents=True, exist_ok=True)
    create_structure(root=root, overwrite=args.overwrite)
    print(f"Architecture prepared in: {root}")


if __name__ == "__main__":
    main()
