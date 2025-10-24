from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Make DATABASE_URL optional so importing the module doesn't raise immediately.
    # Provide a helpful accessor that raises if not set, or change the default to a dev DB.
    DATABASE_URL: Optional[str] = "postgresql+asyncpg://vananhduy:daziel@localhost:5432/bookly_db"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

    def database_url(self) -> str:
        """
        Return DATABASE_URL or raise a clear error guiding the user to set it.
        """
        if not self.DATABASE_URL:
            raise RuntimeError(
                "DATABASE_URL is not set. Set DATABASE_URL in your environment or in .env."
            )
        return self.DATABASE_URL

Config = Settings()