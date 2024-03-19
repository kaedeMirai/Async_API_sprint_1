import orjson
from pydantic import BaseModel


def orjson_dumbs(v, *, default):
    return orjson.dumps(v, default=default).decode()


class BaseModelOrjson(BaseModel):
    class Config:
        json_loads = orjson.loads
        json_dumbs = orjson_dumbs
