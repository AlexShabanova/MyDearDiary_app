from pydantic import BaseModel
from pydantic_settings import BaseSettings


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8080


class ApiPrefixConfig(BaseModel):
    prefix: str = "/api"


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefixConfig = ApiPrefixConfig()


settings = Settings()
