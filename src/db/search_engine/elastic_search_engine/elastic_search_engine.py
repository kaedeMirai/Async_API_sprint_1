from elasticsearch import AsyncElasticsearch, NotFoundError, RequestError
import orjson

from exceptions.exceptions import BadParamException
from dto.query_params_dto import QueryParamsDTO
from db.search_engine.async_search_engine import AsyncSearchEngine
from db.search_engine.elastic_search_engine.request_body_templates import (
    generate_request_body_with_filtering,
    generate_request_body_without_filtering
)


class ElasticSearchEngine(AsyncSearchEngine):
    def __init__(self, elastic: AsyncElasticsearch):
        self.elastic = elastic

    async def search_doc_by_id(self, index: str, doc_id: str) -> bytes | None:
        try:
            doc = await self.elastic.get(index=index, id=doc_id)
        except NotFoundError:
            return None

        return orjson.dumps(doc['_source'])

    async def search_multiple_docs(self, index: str, query_dto: QueryParamsDTO):
        request_body = self._generate_request_for_multiple_docs(query_dto)
        docs = await self._retrieve_docs(index, request_body)

        return docs

    async def _retrieve_docs(self, index: str, request_body: str) -> bytes | None:
        try:
            response = await self.elastic.search(index=index, body=request_body)
        except NotFoundError:
            return None
        except RequestError:
            raise BadParamException('Bad request param specified.')
        return orjson.dumps([doc['_source'] for doc in response['hits']['hits']])

    def _generate_request_for_multiple_docs(self, query_dto: QueryParamsDTO) -> str:
        if query_dto.query:
            query = generate_request_body_with_filtering(query_dto)
        else:
            query = generate_request_body_without_filtering(query_dto)

        return query
