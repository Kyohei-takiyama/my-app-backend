import os

from functools import lru_cache
from pydantic_settings import BaseSettings

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Environment(BaseSettings):
    """環境変数を読み込む"""

    API_ENV: str
    LOG_LEVEL: str
    FRONTEND_URL: str
    DATABASE_URL: str
    database_url: str
    SECRET_KEY: str
    ALGORITHM: str
    DEBUG: str

    class Config:
        env = os.getenv("API_ENV", default="local")
        env_file = os.path.join(PROJECT_ROOT + "/core/envs", f".env.{env}")


@lru_cache
def get_env():
    """@lru_cacheで.envの結果をキャッシュする"""
    return Environment()
