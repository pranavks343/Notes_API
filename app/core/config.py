from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    app_name: str = "Notes API"
    api_v1_prefix: str = "/api/v1"
    database_url: str = "sqlite:///./app.db"   # ← new

settings = Settings()