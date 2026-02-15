"""Simple SQL migration runner."""

from pathlib import Path

from app.infrastructure.db.sqlite.connection import get_connection


def run_migrations(db_path: str, migrations_dir: str = "app/infrastructure/db/sqlite/migrations") -> None:
    sql_files = sorted(Path(migrations_dir).glob("*.sql"))
    with get_connection(db_path) as conn:
        for sql_file in sql_files:
            conn.executescript(sql_file.read_text(encoding="utf-8"))
