from dataclasses import dataclass
from typing import Optional

from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class Database:
    db_host: str
    db_port: str
    db_name: str
    db_user: str
    db_pass: str


@dataclass
class Redis:
    host: str
    port: int
    db: int


@dataclass
class Config:
    tg_bot: TgBot
    database: Database
    redis: Redis


def load_config(path: Optional[str] = None) -> Config:
    env = Env()
    env.read_env()
    return Config(
        tg_bot=TgBot(
            token=env("BOT_TOKEN"),
        ),
        database=Database(
            db_host=env("DB_HOST"),
            db_port=env("DB_PORT"),
            db_name=env("DB_NAME"),
            db_user=env("DB_USER"),
            db_pass=env("DB_PASS"),
        ),
        redis=Redis(
            host=env("REDIS_HOST"),
            port=env.int("REDIS_PORT"),
            db=env.int("REDIS_DB"),
        )
    )
