from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    app_name: str = "Backend POC"
    debug: bool = True
settings = Settings()