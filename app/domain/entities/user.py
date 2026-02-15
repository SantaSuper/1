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
