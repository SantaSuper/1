"""Use cases for registration flow."""

from dataclasses import dataclass

from app.domain.entities.faction import is_valid_faction
from app.infrastructure.repositories.pending_repository import PendingApprovalRepository


@dataclass(slots=True)
class RegistrationRequest:
    vk_id: int
    nickname: str
    faction: str
    desired_position: str
    rp_name: str


class RegisterUserUseCase:
    def __init__(self, pending_repo: PendingApprovalRepository) -> None:
        self._pending_repo = pending_repo

    def execute(self, request: RegistrationRequest) -> int:
        if not is_valid_faction(request.faction):
            raise ValueError("Неизвестная фракция")
        if not request.nickname.strip():
            raise ValueError("Ник не может быть пустым")
        return self._pending_repo.create(
            vk_id=request.vk_id,
            nickname=request.nickname.strip(),
            faction=request.faction,
            desired_position=request.desired_position.strip(),
            rp_name=request.rp_name.strip(),
        )
