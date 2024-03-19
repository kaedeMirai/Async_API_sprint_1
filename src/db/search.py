from elasticsearch import AsyncElasticsearch

from db.search_engine.async_search_engine import AsyncSearchEngine
from db.search_engine.elastic_search_engine.elastic_search_engine import ElasticSearchEngine

search_client: AsyncElasticsearch | None


async def get_search_engine() -> AsyncSearchEngine | None:
    return ElasticSearchEngine(search_client)
