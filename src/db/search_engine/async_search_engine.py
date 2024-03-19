from abc import abstractmethod, ABC
from dto.query_params_dto import QueryParamsDTO


class AsyncSearchEngine(ABC):
    @abstractmethod
    async def search_doc_by_id(self, index, doc_id):
        pass

    @abstractmethod
    async def search_multiple_docs(self, index, query_dto: QueryParamsDTO):
        pass
