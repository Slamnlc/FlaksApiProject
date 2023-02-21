import hashlib
import logging
from functools import lru_cache
from secrets import token_urlsafe
from typing import Union

from flask import request

from config import Folders


def generate_token(nbytes: int = 100) -> str:
    return token_urlsafe(nbytes)


@lru_cache
def hash_text(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()


def create_logger(name: str = None) -> logging.Logger:
    if not name:
        name = "logger"
    log_file = Folders.LOGGING_DIR.joinpath(f"{name}.log")
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(log_file)
    console_handler.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "[%(levelname)s]:%(asctime)s:%(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger


def get_current_token() -> Union[str, None]:
    auth = request.headers.get("Authorization")
    if not auth or "bearer " not in auth.lower():
        return None
    return auth.split(" ")[-1]
