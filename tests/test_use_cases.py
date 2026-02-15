from pathlib import Path

from app.application.use_cases import RegisterUserUseCase, RegistrationRequest, UseInviteCodeUseCase
from app.domain.entities.invite_code import InviteCode
from app.infrastructure.db.sqlite.migrator import run_migrations
from app.infrastructure.repositories import InviteCodeRepository, PendingApprovalRepository, UserRepository


def test_register_request_creates_pending_row(tmp_path: Path) -> None:
    db = tmp_path / "test.db"
    run_migrations(str(db))

    use_case = RegisterUserUseCase(PendingApprovalRepository(str(db)))
    request_id = use_case.execute(
        RegistrationRequest(
            vk_id=1,
            nickname="Tester",
            faction="МВД",
            desired_position="Стажёр",
            rp_name="Тест Тестов",
        )
    )

    assert request_id > 0


def test_invite_code_registers_user(tmp_path: Path) -> None:
    db = tmp_path / "test.db"
    run_migrations(str(db))

    invite_repo = InviteCodeRepository(str(db))
    user_repo = UserRepository(str(db))

    invite_repo.save(InviteCode(code="ABC123", faction="СМИ", level=1, position="Редактор", rp_name="РП Имя"))
    use_case = UseInviteCodeUseCase(invite_repo, user_repo)

    user = use_case.execute(vk_id=99, nickname="Nick99", code="ABC123")

    assert user.registered is True
    assert user.faction == "СМИ"
    persisted = user_repo.get(99)
    assert persisted is not None
    assert persisted.nickname == "Nick99"
