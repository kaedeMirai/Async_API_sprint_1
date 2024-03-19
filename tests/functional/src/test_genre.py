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

GENRES_ENDPOINT = 'genres'

GOOD_ID = 'b92ef010-5e4c-4fd0-99d6-41b6456272cd'


@pytest.mark.parametrize('query_data, expected_answer',
                         [({'query': 'music', 'page_size': 10}, {'status': HTTPStatus.OK, 'length': 1}),
                          ({'query': 'abcde', 'page_size': 10}, {'status': HTTPStatus.OK, 'length': 0}),
                          ({'query': '', 'page_size': 100}, {'status': HTTPStatus.OK, 'length': 10})])
@pytest.mark.asyncio
async def test_search(make_get_request, query_data: dict, expected_answer: dict):
    response = await make_get_request(GENRES_ENDPOINT, query_data)

    assert response['status'] == expected_answer['status']
    assert len(response['body']) == expected_answer['length']


@pytest.mark.parametrize('query_data, expected_answer',
                         [('1cacff68-643e-4ddd-8f57-84b62538081a', {'status': HTTPStatus.OK, 'length': 3}),
                          ('aaaaaaaa-1111-aaaa-aaaa-aaaaaaaaaaaa', {'status': HTTPStatus.OK, 'length': 0})])
@pytest.mark.asyncio
async def test_genre_by_id(make_get_request, query_data: dict, expected_answer: dict):
    response = await make_get_request(f'{GENRES_ENDPOINT}/{query_data}')

    assert response['status'] == expected_answer['status']
    assert len(response['body']) == expected_answer['length']


@pytest.mark.asyncio
async def test_get_genres_with_valid_data(make_get_request):
    params = get_default_query_params()
    response = await make_get_request(GENRES_ENDPOINT, params)

    assert response['status'] == HTTPStatus.OK
    assert response['body'] == [{"id": GOOD_ID, "name": "Fantasy", "description": None}]


@pytest.mark.asyncio
async def test_get_genres_with_invalid_sort_by(make_get_request):
    params = get_default_query_params()
    params['sort_by'] = 'name'

    response = await make_get_request(GENRES_ENDPOINT, params)

    assert response['status'] == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response['body'] is None


@pytest.mark.asyncio
async def test_get_genres_with_invalid_sorting_order(make_get_request):
    params = get_default_query_params()
    params['sorting_order'] = 'invalid_data'

    response = await make_get_request(GENRES_ENDPOINT, params)

    assert response['status'] == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response['body'] is None


@pytest.mark.asyncio
async def test_get_genres_with_invalid_page_size(make_get_request):
    params = get_default_query_params()
    params['page_size'] = 10001

    response = await make_get_request(GENRES_ENDPOINT, params)

    assert response['status'] == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response['body'] is None


@pytest.mark.asyncio
async def test_retrieve_from_cache(delete_doc, make_get_request, clear_cache):
    await clear_cache

    index = test_settings.es_index_mapping['genres']
    await delete_doc(index=index, doc_id=GOOD_ID)

    response = await make_get_request(f'{GENRES_ENDPOINT}/{GOOD_ID}')

    assert response['status'] == HTTPStatus.OK
    assert response['body'] == {}


def get_default_query_params():
    return {
        'query': 'Fantasy',
        'page_size': 10,
        'offset': 0,
        'sort_by': 'id',
        'sorting_order': 'asc',
    }
