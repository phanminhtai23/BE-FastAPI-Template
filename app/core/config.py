# app/core/config.py
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    DATABASE_URL: str                    # ✅ Bắt buộc phải có
    SECRET_KEY: str = Field(..., min_length=32)      # ✅ Có default value
    DEBUG: bool = False                  # ✅ Auto convert sang bool
    PORT: int = Field(default=8000, ge=1000, le=65535)  # ✅ 1000-65535

    HOST: str = "0.0.0.0"                  # ✅ Auto convert sang int
    API_V1_STR: str = "/api/v1"          # ✅ Auto convert sang str
    
    class Config:
        env_file = ".env"                # ✅ Tự động load .env

settings = Settings()  # ✅ Validate ngay khi import