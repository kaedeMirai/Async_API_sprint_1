from redis.asyncio import Redis

from db.cache_storage.async_cache_storage import AsyncCacheStorage
from db.cache_storage.redis_cache_storage import RedisCacheStorage

cache_client: Redis | None


async def get_cache_storage() -> AsyncCacheStorage | None:
    return RedisCacheStorage(cache_client)


