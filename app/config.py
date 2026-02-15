"""Centralized configuration for the bot."""

from dataclasses import dataclass
import os


@dataclass(slots=True)
class Settings:
    vk_group_token: str
    vk_group_id: int
    sqlite_path: str = "data/rw1.db"
    app_mode: str = "local"


def load_settings() -> Settings:
    return Settings(
        vk_group_token=os.getenv("VK_GROUP_TOKEN", ""),
        vk_group_id=int(os.getenv("VK_GROUP_ID", "0")),
        sqlite_path=os.getenv("SQLITE_PATH", "data/rw1.db"),
        app_mode=os.getenv("APP_MODE", "local"),
    )
