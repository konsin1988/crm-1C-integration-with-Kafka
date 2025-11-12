from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    PROJECT_NAME: str 
    ENVIRONMENT: str = "dev"

    DB_HOST: str
    DB_PORT: int = 3306 
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    BASE_LINK: str
    
    KAFKA_BOOTSTRAP_SERVERS: str
    KAFKA_GUID_TOPIC: str

    @property
    def DATABASE_URL(self) -> str:
        return (
                f"mysql+aiomysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
               )

    @property
    def DB_CONFIG(self) -> dict:
        return {
            "host": self.DB_HOST,
            "port": self.DB_PORT,
            "user": self.DB_USER,
            "password": self.DB_PASSWORD,
            "db": self.DB_NAME
                }

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()
