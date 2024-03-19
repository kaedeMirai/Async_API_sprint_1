from .base_model import BaseModelOrjson


class Actor(BaseModelOrjson):
    id: str
    name: str


class Writer(BaseModelOrjson):
    id: str
    name: str


class Film(BaseModelOrjson):
    id: str
    title: str
    description: str | None
    genre: list[str] | None
    imdb_rating: float
    director: list[str] | list
    actors: list[Actor] | None
    writers: list[Writer] | None
    actors_names: list[str] | list
    writers_names: list[str] | list
