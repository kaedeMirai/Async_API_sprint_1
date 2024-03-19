from functools import lru_cache

from fastapi import Depends

from db.cache import get_cache_storage
from db.search import get_search_engine

from db.cache_storage.async_cache_storage import AsyncCacheStorage
from db.search_engine.async_search_engine import AsyncSearchEngine

from services.base_service import BaseService
from models.film import Film


class FilmService(BaseService):
    SEARCH_INDEX = 'movies'

    def __init__(self, cache_storage: AsyncCacheStorage, search_engine: AsyncSearchEngine):
        self.cache_storage = cache_storage
        self.search_engine = search_engine
        super().__init__(Film, self.cache_storage, self.search_engine, self.SEARCH_INDEX)


@lru_cache()
def get_film_service(
        cache_storage: AsyncCacheStorage = Depends(get_cache_storage),
        search_engine: AsyncSearchEngine = Depends(get_search_engine),
) -> FilmService:
    return FilmService(cache_storage, search_engine)
