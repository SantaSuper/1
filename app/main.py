"""Application entrypoint."""

from app.presentation.vk.runner import start_polling


if __name__ == "__main__":
    start_polling()
