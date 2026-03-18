from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    API_KEY: str
    DATABASE_URL: str

    model_config = SettingsConfigDict(env_file="app/db/.env")

    @property
    def ASYNC_DATABASE_URL(self):
        return f"sqlite+aiosqlite:///{self.DATABASE_URL}"

settings = Settings()  # type: ignore
