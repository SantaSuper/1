"""Bootstrap demo data for local run / Google Colab."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.config import load_settings
from app.domain.entities.invite_code import InviteCode
from app.infrastructure.db.sqlite.migrator import run_migrations
from app.infrastructure.repositories.invite_repository import InviteCodeRepository


def main() -> None:
    settings = load_settings()
    run_migrations(settings.sqlite_path)

    invite_repo = InviteCodeRepository(settings.sqlite_path)
    invite_repo.save(
        InviteCode(
            code="RW1001",
            faction="МВД",
            level=1,
            position="Стажёр",
            rp_name="Иван Петров",
        )
    )
    print("Demo invite code created: RW1001")


if __name__ == "__main__":
    main()
