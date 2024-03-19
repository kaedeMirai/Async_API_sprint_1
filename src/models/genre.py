from .base_model import BaseModelOrjson


class Genre(BaseModelOrjson):
    id: str
    name: str
    description: str | None
