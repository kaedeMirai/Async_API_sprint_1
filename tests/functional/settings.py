from pydantic import Field
from pydantic_settings import BaseSettings


class TestSettings(BaseSettings):
    es_host: str = Field(default='http://127.0.0.1', json_schema_extra={'env': 'ES_HOST'})
    es_port: str = Field(default='9200', json_schema_extra={'env': 'ES_PORT'})
    es_id_field: str = Field('id')
    es_index_mapping: dict = {
        'movies': 'movies',
        'genres': 'genres',
        'persons': 'persons'
    }
    redis_host: str = Field(default='127.0.0.1', json_schema_extra={'env': 'REDIS_HOST'})
    redis_port: str = Field(default='6379', json_schema_extra={'env': 'REDIS_PORT'})
    service_url: str = 'http://nginx:80/api/v1/'

    class Config:
        env_file = ".env.example"


test_settings = TestSettings()
