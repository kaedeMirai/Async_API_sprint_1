import base64
from dto.query_params_dto import QueryParamsDTO


def generate_key_based_on_query_dto_and_model_name(query_dto: QueryParamsDTO, model_name: str) -> str:
    key = ''

    if query_dto.query:
        key += str(query_dto.query)
    else:
        key += 'all'

    key += model_name + str(query_dto.page_size) + str(query_dto.offset) \
            + str(query_dto.sort_by) + str(query_dto.sorting_order)

    return base64.b64encode(key.encode()).decode()
