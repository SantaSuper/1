"""Use case for joining with invite code."""

from app.domain.entities.user import User
from app.infrastructure.repositories.invite_repository import InviteCodeRepository
from app.infrastructure.repositories.user_repository import UserRepository


class UseInviteCodeUseCase:
    def __init__(self, invite_repo: InviteCodeRepository, user_repo: UserRepository) -> None:
        self._invite_repo = invite_repo
        self._user_repo = user_repo

    def execute(self, vk_id: int, nickname: str, code: str) -> User:
        invite = self._invite_repo.get(code)
        if not invite or invite.used:
            raise ValueError("Код не найден или уже использован")
        if invite.target_vk_id and invite.target_vk_id != vk_id:
            raise ValueError("Код привязан к другому VK ID")

        user = User(
            vk_id=vk_id,
            nickname=nickname,
            faction=invite.faction,
            position=invite.position,
            rp_name=invite.rp_name,
            registered=True,
        )
        self._user_repo.save(user)
        self._user_repo.set_level(vk_id=vk_id, faction=invite.faction, level=invite.level)
        self._invite_repo.mark_used(code)
        return user
