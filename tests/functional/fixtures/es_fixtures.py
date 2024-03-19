import json
import pathlib
import pytest
import pytest_asyncio

from elasticsearch import AsyncElasticsearch

from tests.functional.settings import test_settings
import tests.functional.test_data.es_mapping as es_mapping

BASE_FILE_PATH = pathlib.Path(__file__).parents[1] / 'test_data'

TEST_DATA_FILE_NAMES = {
    'movies': 'movies_test_data.json',
    'genres': 'genres_test_data.json',
    'persons': 'persons_test_data.json'
}

INDICES_MAPPINGS = {
    'movies': {
        'name': test_settings.es_index_mapping['movies'],
        'settings': es_mapping.MOVIES_INDEX_SETTINGS,
        'mappings': es_mapping.MOVIES_INDEX_MAPPINGS,
        'file_path': f'{BASE_FILE_PATH}/{TEST_DATA_FILE_NAMES["movies"]}'
    },
    'genres': {
        'name': test_settings.es_index_mapping['genres'],
        'settings': es_mapping.GENRES_INDEX_SETTINGS,
        'mappings': es_mapping.GENRES_INDEX_MAPPINGS,
        'file_path': f'{BASE_FILE_PATH}/{TEST_DATA_FILE_NAMES["genres"]}'
    },
    'persons': {
        'name': test_settings.es_index_mapping['persons'],
        'settings': es_mapping.PERSONS_INDEX_SETTINGS,
        'mappings': es_mapping.PERSONS_INDEX_MAPPINGS,
        'file_path': f'{BASE_FILE_PATH}/{TEST_DATA_FILE_NAMES["persons"]}'
    }
}


@pytest_asyncio.fixture(scope='session')
async def es_connect(event_loop):
    host = f'{test_settings.es_host}:{test_settings.es_port}'
    client = AsyncElasticsearch(hosts=host,
                                validate_cert=False,
                                use_ssl=False)
    yield client
    await client.close()


@pytest_asyncio.fixture(scope='session', autouse=True)
async def create_test_data(es_connect):
    es_client = es_connect
    await load_test_data_to_elastic(es_client)
    yield
    await delete_indices(es_client)


@pytest.mark.asyncio
async def load_test_data_to_elastic(es_client):
    for index in INDICES_MAPPINGS:
        index_info = INDICES_MAPPINGS[index]
        await create_index(index_info, es_client)
        await load_data_to_index(index_info['file_path'], index_info['name'], es_client)


@pytest.mark.asyncio
async def create_index(index_info, es_client: AsyncElasticsearch):
    index = index_info['name']
    is_index_exists = await check_if_index_exists(index, es_client)

    if is_index_exists:
        return

    request_body = {
        'settings': index_info['settings'],
        'mappings': index_info['mappings']
    }

    await es_client.indices.create(index=index, body=request_body)


@pytest.mark.asyncio
async def load_data_to_index(file_path, index, es_client: AsyncElasticsearch):
    data = extract_data_from_json_file(file_path)
    bulk_query = create_es_bulk_query(data, index)

    response = await es_client.bulk(bulk_query, refresh=True)

    if response['errors']:
        raise Exception(f'Error loading data to {index} index.')


@pytest.mark.asyncio
async def check_if_index_exists(index, es_client: AsyncElasticsearch):
    is_index_exists = await es_client.indices.exists(index=index)
    return is_index_exists


def extract_data_from_json_file(file_path):
    with open(file_path, encoding='utf-8') as file:
        data = json.load(file)
    return data


def create_es_bulk_query(data, index):
    bulk_query = []
    for row in data:
        bulk_query.extend([
            json.dumps({'index': {
                '_index': index,
                '_id': row[test_settings.es_id_field]
            }}),
            json.dumps(row)
        ])

    str_query = '\n'.join(bulk_query) + '\n'

    return str_query


@pytest.mark.asyncio
async def delete_indices(es_client: AsyncElasticsearch):
    for index in INDICES_MAPPINGS:
        index_name = INDICES_MAPPINGS[index]['name']
        is_index_exists = await check_if_index_exists(index_name, es_client)

        if is_index_exists:
            await es_client.indices.delete(index=index_name)


@pytest.fixture
def delete_doc(es_connect):
    async def inner(index, doc_id):
        es_client = es_connect
        await es_client.delete(index=index, id=doc_id, refresh='wait_for')

    return inner
