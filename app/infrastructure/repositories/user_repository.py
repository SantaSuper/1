"""Repository for user persistence."""

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
                (user.vk_id, user.nickname, user.faction, user.position, user.rp_name, int(user.registered)),
            )

    def get(self, vk_id: int) -> User | None:
        with get_connection(self._db_path) as conn:
            row = conn.execute("SELECT * FROM users WHERE vk_id = ?", (vk_id,)).fetchone()
            if not row:
                return None
            return User(
                vk_id=row["vk_id"],
                nickname=row["nickname"],
                faction=row["faction"],
                position=row["position"],
                rp_name=row["rp_name"],
                registered=bool(row["registered"]),
            )

    def set_level(self, vk_id: int, faction: str, level: int) -> None:
        with get_connection(self._db_path) as conn:
            conn.execute(
                """
                INSERT INTO user_levels(vk_id, faction, level)
                VALUES(?, ?, ?)
                ON CONFLICT(vk_id, faction) DO UPDATE SET level = excluded.level
                """,
                (vk_id, faction, level),
            )
