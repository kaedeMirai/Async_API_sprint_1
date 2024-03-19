import pytest
from http import HTTPStatus

from tests.functional.settings import test_settings

from tests.functional.conftest import (
    es_connect,
    event_loop,
    create_test_data,
    make_get_request,
    delete_doc,
    redis_connect,
    clear_cache
)

GOOD_ID = '0031feab-8f53-412a-8f53-47098a60ac73'

BAD_ID = '11111111-1111-4d66-adbe-50eb917f463a'

PERSONS_ENDPOINT = 'persons'


@pytest.mark.parametrize(
    'query_info, expected_answer',
    [
        (
                {'query': 'Naohisa Inoue'},
                {'status': HTTPStatus.OK, 'length': 1}
        ),
        (
                {'query': 'ABCDEFGH'},
                {'status': HTTPStatus.OK, 'length': 0}
        )
    ]
)
@pytest.mark.asyncio
async def test_search(make_get_request, query_info, expected_answer):
    query_params = get_default_query_params()
    query_params['query'] = query_info['query']

    response = await make_get_request(PERSONS_ENDPOINT, query_params)

    assert response['status'] == expected_answer['status']
    assert len(response['body']) == expected_answer['length']


@pytest.mark.asyncio
async def test_all_persons(make_get_request):
    query_params = get_default_query_params()

    response = await make_get_request(PERSONS_ENDPOINT, query_params)

    assert response['status'] == HTTPStatus.OK
    assert len(response['body']) == 10


@pytest.mark.asyncio
async def test_person_by_id_good_id(make_get_request):
    response = await make_get_request(f'{PERSONS_ENDPOINT}/{GOOD_ID}')

    assert response['status'] == HTTPStatus.OK
    assert response['body']['id'] == GOOD_ID


@pytest.mark.asyncio
async def test_person_by_id_bad_id(make_get_request):
    response = await make_get_request(f'{PERSONS_ENDPOINT}/{BAD_ID}')

    assert response['status'] == HTTPStatus.OK
    assert response['body'] == {}


@pytest.mark.asyncio
async def test_bad_page_size_param(make_get_request):
    query_params = get_default_query_params()
    query_params['page_size'] = -1

    response = await make_get_request(PERSONS_ENDPOINT, query_params)

    assert response['status'] == HTTPStatus.UNPROCESSABLE_ENTITY


@pytest.mark.asyncio
async def test_bad_offset_param(make_get_request):
    query_params = get_default_query_params()
    query_params['offset'] = -1

    response = await make_get_request(PERSONS_ENDPOINT, query_params)

    assert response['status'] == HTTPStatus.UNPROCESSABLE_ENTITY


@pytest.mark.asyncio
async def test_bad_sort_by_param(make_get_request):
    query_params = get_default_query_params()
    query_params['sort_by'] = 'bla-bla-bla'

    response = await make_get_request(PERSONS_ENDPOINT, query_params)

    assert response['status'] == HTTPStatus.UNPROCESSABLE_ENTITY


@pytest.mark.asyncio
async def test_bad_sorting_order_param(make_get_request):
    query_params = get_default_query_params()
    query_params['sorting_order'] = 'bla-bla-bla'

    response = await make_get_request(PERSONS_ENDPOINT, query_params)

    assert response['status'] == HTTPStatus.UNPROCESSABLE_ENTITY


@pytest.mark.asyncio
async def test_retrieve_from_cache(delete_doc, make_get_request, clear_cache):
    await clear_cache

    index = test_settings.es_index_mapping['persons']
    await delete_doc(index=index, doc_id=GOOD_ID)

    response = await make_get_request(f'{PERSONS_ENDPOINT}/{GOOD_ID}')

    assert response['status'] == HTTPStatus.OK
    assert response['body'] == {}


def get_default_query_params():
    return {
        'page_size': 100,
        'offset': 0,
        'sort_by': 'id',
        'sorting_order': 'asc'
    }
