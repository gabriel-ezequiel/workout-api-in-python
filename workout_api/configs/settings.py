from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str = Field(default="postgresql+asyncpg://myuser:mypass@host.docker.internal:5432/mydb")

settings = Settings()