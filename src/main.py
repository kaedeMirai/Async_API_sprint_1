import logging
import uvicorn
from elasticsearch import AsyncElasticsearch
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from contextlib import asynccontextmanager
from redis.asyncio import Redis

from db import cache, search

from api.v1 import films
from api.v1 import genres
from api.v1 import persons

from core.config import settings
from core.logger import LOGGING


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with Redis(host=settings.redis_host, port=settings.redis_port) as cache.cache_client, \
            AsyncElasticsearch(hosts=[f'{settings.elastic_host}:{settings.elastic_port}']) as search.search_client:
        app.state.cache_storage = cache.cache_client
        app.state.search_engine = search.search_client
        yield


def build_app():
    app = FastAPI(
        title=settings.project_name,
        description='Information about films, genres and persons',
        version='1.0.0',
        docs_url='/api/openapi',
        openapi_url='/api/openapi.json',
        default_response_class=ORJSONResponse,
        lifespan=lifespan
    )

    app.include_router(films.router, prefix='/api/v1/films', tags=['films'])
    app.include_router(genres.router, prefix='/api/v1/genres', tags=['genres'])
    app.include_router(persons.router, prefix='/api/v1/persons', tags=['persons'])

    return app


app = build_app()

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings.fastapi_host,
        port=settings.fastapi_port,
        log_config=LOGGING,
        log_level=logging.DEBUG,
        reload=True
    )
