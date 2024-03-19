from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    project_name: str = Field(default='movies', env='PROJECT_NAME')
    redis_host: str = Field(env='REDIS_HOST')
    redis_port: int = Field(env='REDIS_PORT')
    elastic_host: str = Field(env='ELASTIC_HOST')
    elastic_port: int = Field(env='ELASTIC_PORT')
    fastapi_host: str = Field(env='FASTAPI_HOST')
    fastapi_port: int = Field(env='FASTAPI_PORT')
    log_level: str = Field(default='DEBUG', env='LOG_LEVEL')

    class Config:
        env_file = '../../.env'


settings = Settings()
