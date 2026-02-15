"""Repository for invitation code operations."""

from app.domain.entities.invite_code import InviteCode
from app.infrastructure.db.sqlite.connection import get_connection


class InviteCodeRepository:
    def __init__(self, db_path: str) -> None:
        self._db_path = db_path

    def save(self, invite: InviteCode) -> None:
        with get_connection(self._db_path) as conn:
            conn.execute(
                """
                INSERT INTO invite_codes(code, target_vk_id, faction, level, position, rp_name, is_leader, used)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(code) DO UPDATE SET
                    target_vk_id=excluded.target_vk_id,
                    faction=excluded.faction,
                    level=excluded.level,
                    position=excluded.position,
                    rp_name=excluded.rp_name,
                    is_leader=excluded.is_leader,
                    used=excluded.used
                """,
                (
                    invite.code,
                    invite.target_vk_id,
                    invite.faction,
                    invite.level,
                    invite.position,
                    invite.rp_name,
                    int(invite.is_leader),
                    int(invite.used),
                ),
            )

    def get(self, code: str) -> InviteCode | None:
        with get_connection(self._db_path) as conn:
            row = conn.execute("SELECT * FROM invite_codes WHERE code = ?", (code,)).fetchone()
            if not row:
                return None
            return InviteCode(
                code=row["code"],
                target_vk_id=row["target_vk_id"],
                faction=row["faction"],
                level=row["level"],
                position=row["position"],
                rp_name=row["rp_name"],
                is_leader=bool(row["is_leader"]),
                used=bool(row["used"]),
            )

    def mark_used(self, code: str) -> None:
        with get_connection(self._db_path) as conn:
            conn.execute("UPDATE invite_codes SET used = 1 WHERE code = ?", (code,))
