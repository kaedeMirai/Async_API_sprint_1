from redis.asyncio import Redis

from db.cache_storage.async_cache_storage import AsyncCacheStorage


class RedisCacheStorage(AsyncCacheStorage):
    CACHE_EXPIRE_IN_SECONDS = 60 * 5

    def __init__(self, redis: Redis):
        self.redis = redis

    async def get(self, key: str, **kwargs):
        data = await self.redis.get(key)
        return data

    async def set(self, key: str, data: str | bytes, **kwargs):
        await self.redis.set(key, data, self.CACHE_EXPIRE_IN_SECONDS)
