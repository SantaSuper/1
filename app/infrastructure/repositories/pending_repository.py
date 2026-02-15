"""Repository for pending registration approvals."""

from app.infrastructure.db.sqlite.connection import get_connection


class PendingApprovalRepository:
    def __init__(self, db_path: str) -> None:
        self._db_path = db_path

    def create(self, vk_id: int, nickname: str, faction: str, desired_position: str, rp_name: str) -> int:
        with get_connection(self._db_path) as conn:
            cur = conn.execute(
                """
                INSERT INTO pending_approvals(vk_id, nickname, faction, desired_position, rp_name)
                VALUES(?, ?, ?, ?, ?)
                """,
                (vk_id, nickname, faction, desired_position, rp_name),
            )
            return int(cur.lastrowid)

    def set_status(self, request_id: int, status: str) -> None:
        with get_connection(self._db_path) as conn:
            conn.execute("UPDATE pending_approvals SET status = ? WHERE id = ?", (status, request_id))
