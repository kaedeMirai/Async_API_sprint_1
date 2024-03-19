import orjson

from models.film import Film
from models.genre import Genre
from models.person import Person

from dto.query_params_dto import QueryParamsDTO
from db.cache_storage.async_cache_storage import AsyncCacheStorage
from db.search_engine.async_search_engine import AsyncSearchEngine
from services.util.generate_key import generate_key_based_on_query_dto_and_model_name as generate_key

MODEL_TYPE = Film | Genre | Person | dict


class BaseService:

    def __init__(
            self,
            model_type: MODEL_TYPE,
            cache_storage: AsyncCacheStorage,
            search_engine: AsyncSearchEngine,
            index: str
    ):
        self.model_type = model_type  # type: MODEL_TYPE
        self.cache_storage = cache_storage
        self.search_engine = search_engine
        self.index = index

    async def retrieve_by_id(self, object_id: str) -> MODEL_TYPE:
        object_json = await self.cache_storage.get(object_id)

        if not object_json:
            object_json = await self.search_engine.search_doc_by_id(self.index, object_id)

            if object_json:
                await self.cache_storage.set(object_id, object_json)

        converted_object = {}
        if object_json:
            converted_object = self.model_type.model_validate_json(object_json)

        return converted_object

    async def retrieve_multiple(self, query_dto: QueryParamsDTO) -> list[MODEL_TYPE] | list:
        cache_key = generate_key(query_dto, self.model_type.__name__)
        objects_json = await self.cache_storage.get(cache_key)

        if not objects_json:
            objects_json = await self.search_engine.search_multiple_docs(self.index, query_dto)

            if objects_json:
                await self.cache_storage.set(cache_key, objects_json)

        converted_objects = []
        if objects_json:
            converted_objects = [self.model_type(**object_dict) for object_dict in orjson.loads(objects_json)]

        return converted_objects
