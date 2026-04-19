from .log import setup_logging

setup_logging()

from .server import run_server  # noqa: E402


def main() -> None:
    run_server()


if __name__ == "__main__":
    main()
