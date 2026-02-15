"""Faction constants and validation helpers."""

FACTIONS = ("Армия", "МВД", "СМИ", "Политика", "ФСБ", "Больница")


def is_valid_faction(name: str) -> bool:
    return name in FACTIONS
