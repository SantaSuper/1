"""Local runner with simple command simulation for Colab/dev.

This is a temporary shell until real VK SDK handlers are connected.
"""

from app.application.use_cases import RegisterUserUseCase, RegistrationRequest, UseInviteCodeUseCase
from app.config import load_settings
from app.infrastructure.db.sqlite.migrator import run_migrations
from app.infrastructure.repositories import InviteCodeRepository, PendingApprovalRepository, UserRepository


def start_polling() -> None:
    settings = load_settings()
    run_migrations(settings.sqlite_path)

    user_repo = UserRepository(settings.sqlite_path)
    pending_repo = PendingApprovalRepository(settings.sqlite_path)
    invite_repo = InviteCodeRepository(settings.sqlite_path)

    register_uc = RegisterUserUseCase(pending_repo)
    invite_uc = UseInviteCodeUseCase(invite_repo, user_repo)

    print("RW1 bot core ready. Commands: register | invite | exit")
    while True:
        cmd = input("command> ").strip().lower()
        if cmd == "exit":
            print("Bye")
            return
        if cmd == "register":
            vk_id = int(input("VK ID: ").strip())
            nickname = input("Nick: ").strip()
            faction = input("Faction: ").strip()
            position = input("Desired position: ").strip()
            rp_name = input("RP name: ").strip()
            req_id = register_uc.execute(
                RegistrationRequest(
                    vk_id=vk_id,
                    nickname=nickname,
                    faction=faction,
                    desired_position=position,
                    rp_name=rp_name,
                )
            )
            print(f"Заявка создана: #{req_id}")
            continue
        if cmd == "invite":
            vk_id = int(input("VK ID: ").strip())
            nickname = input("Nick: ").strip()
            code = input("Code: ").strip()
            user = invite_uc.execute(vk_id=vk_id, nickname=nickname, code=code)
            print(f"Успех: {user.nickname} принят во фракцию {user.faction}")
            continue
        print("Unknown command")
