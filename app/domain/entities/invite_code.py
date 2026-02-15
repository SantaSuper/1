"""Domain entity: invitation code."""

from dataclasses import dataclass


@dataclass(slots=True)
class InviteCode:
    code: str
    faction: str
    level: int
    target_vk_id: int | None = None
    position: str | None = None
    rp_name: str | None = None
    is_leader: bool = False
    used: bool = False
