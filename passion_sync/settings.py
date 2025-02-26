from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url_async: str
    test_database_url_async: str
    database_url: str
    test_database_url: str
    echo_sql: bool = False
    test: bool = True
    

settings = Settings()