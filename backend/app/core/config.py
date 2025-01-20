from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_HOST: str
    MYSQL_DATABASE: str
    DATABASE_URL: Optional[str] = None  # Optional mit Default None

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        """Get DB URL."""
        return (
            f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}"
            f"@{self.MYSQL_HOST}/{self.MYSQL_DATABASE}"
        )

    model_config = SettingsConfigDict(env_file=".env")


# Erstelle Settings-Instanz
settings = Settings()
