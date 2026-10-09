from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    MODE: Literal["DEV","PROD"] = "DEV"
    SECRET_ADMIN_TOKEN: str = "dev_token"

    TG_BOT_APIKEY: str
    TG_ADMIN_CHAT_IDS: list[int]
    TG_PROXY: str

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    FRONTEND_PORT: int

    @property # Getter - В ООП используется для методов получения данных
    def DB_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env"
    )

settings = Settings()
