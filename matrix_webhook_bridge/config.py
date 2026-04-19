import logging
import os

logger = logging.getLogger(__name__)


def _require_env(var: str) -> str:
    val = os.environ.get(var)
    if not val:
        logger.critical(f"Required environment variable {var} is not set.")
        raise RuntimeError(f"Required environment variable {var} is not set.")
    return val


BASE_URL = _require_env("MATRIX_BASE_URL")  # e.g. https://matrix.example.com
ROOM_ID = _require_env("MATRIX_ROOM_ID")    # e.g. !abc123:matrix.example.com
DOMAIN = _require_env("MATRIX_DOMAIN")      # e.g. matrix.example.com

DEFAULT_USER = "jeeves"
