from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8080


class ApiPrefixConfig(BaseModel):
    prefix: str = "/api"


class DatabaseConfig(BaseModel):
    # FIXME без значения по умолчанию не работает
    # to create db engine
    url: PostgresDsn = "postgres://postgres:postgres@localhost:5432/MyDearDiary_service"
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefixConfig = ApiPrefixConfig()
    db: DatabaseConfig = DatabaseConfig()


settings = Settings()
