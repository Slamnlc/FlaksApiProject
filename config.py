from pathlib import Path


class Folders:
    BASE_DIR = Path(__file__).parent
    DATABASE_DIR = BASE_DIR.joinpath("database")
    LOGGING_DIR = BASE_DIR.joinpath("logging")
    LOGGING_DIR.mkdir(exist_ok=True)


class DatabaseConfig:
    FILE_NAME = "db.db"
    FILE_LOCATION = Folders.DATABASE_DIR.joinpath(FILE_NAME)
    CONNECTION_URL = f"sqlite:///{FILE_LOCATION}"


class Config:
    BASE_DIR = Path(__file__).parent
    DATABASE_DIR = BASE_DIR.joinpath("database")
    API_EXPIRE_MIN = 60
    ADMIN_USER = "admin"
    ADMIN_PASS = "admin"
