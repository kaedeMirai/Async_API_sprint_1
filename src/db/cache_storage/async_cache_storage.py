from abc import abstractmethod, ABC


class AsyncCacheStorage(ABC):
    @abstractmethod
    async def get(self, key: str, **kwargs):
        pass

    @abstractmethod
    async def set(self, key: str, data: str | bytes, **kwargs):
        pass
