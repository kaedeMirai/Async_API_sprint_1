from dto.query_params_dto import QueryParamsDTO


def generate_request_body_with_filtering(query_dto: QueryParamsDTO):
    return {
        "size": query_dto.page_size,
        "from": query_dto.offset,
        "query": {
            "multi_match": {
                "query": query_dto.query
            }
        },
        "sort": [
            {
                query_dto.sort_by: {
                    "order": query_dto.sorting_order
                }
            }
        ]
    }


def generate_request_body_without_filtering(query_dto: QueryParamsDTO):
    return {
        "size": query_dto.page_size,
        "from": query_dto.offset,
        "query": {
            "match_all": {}
        },
        "sort": [
            {
                query_dto.sort_by: {
                    "order": query_dto.sorting_order
                }
            }
        ]
    }
