from .base_model import BaseModelOrjson


class Person(BaseModelOrjson):
    id: str
    full_name: str
