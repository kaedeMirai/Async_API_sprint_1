import pytest
import pytest_asyncio
from redis.asyncio import Redis

from tests.functional.settings import test_settings


@pytest_asyncio.fixture(scope='session')
async def redis_connect(event_loop):
    client = Redis(host=test_settings.redis_host, port=test_settings.redis_port)
    yield client
    await client.close()


@pytest.fixture
async def clear_cache(redis_connect):
    redis_client = redis_connect
    await redis_client.flushall()
