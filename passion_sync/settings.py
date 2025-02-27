from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

class Settings(BaseSettings):
    database_url_async: str = ""
    test_database_url_async: str = ""
    database_url: str
    test_database_url: str = ""
    echo_sql: bool = False
    async_db: bool = False
    test_db: bool = False
    server_port: int
    metrics_port: int

settings = Settings()