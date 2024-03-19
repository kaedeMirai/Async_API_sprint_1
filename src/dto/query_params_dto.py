from fastapi import Query
from typing import Annotated
from enum import Enum


class SortingOrder(str, Enum):
    ASC = 'asc'
    DESC = 'desc'


class QueryParamsDTO:
    def __init__(
            self,
            query: Annotated[str | None, Query(description='If specified, result will be filtered')] = None,
            page_size: Annotated[int, Query(ge=5, description='Amount of records per page')] = 10,
            offset: Annotated[int, Query(ge=0, description='Skip first X records')] = 0,
            sort_by: Annotated[str | None, Query(description='Name of field to sort by')] = 'id',
            sorting_order: Annotated[SortingOrder | None, Query(description='asc or desc')] = 'asc'
    ):
        self.query = query
        self.page_size = page_size
        self.offset = offset
        self.sort_by = sort_by
        self.sorting_order = sorting_order
