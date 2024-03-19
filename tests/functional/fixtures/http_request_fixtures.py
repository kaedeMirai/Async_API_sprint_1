import logging
import pytest
import pytest_asyncio
import aiohttp
from http import HTTPStatus

from tests.functional.settings import test_settings


@pytest_asyncio.fixture
async def session():
    session = aiohttp.ClientSession()
    yield session
    await session.close()


@pytest.fixture
def make_get_request(session):
    async def inner(endpoint: str, params: dict = None):
        params = params or {}

        try:
            url = f'{test_settings.service_url}{endpoint}'

            async with session.get(url, params=params) as response:
                status = response.status
                if status == HTTPStatus.OK:
                    body = await response.json()
                else:
                    body = None

            return {'body': body, 'status': status}

        except aiohttp.ClientConnectorError as ex:
            logging.error(f'An error occurred: {ex}')
            return {'body': None, 'status': HTTPStatus.INTERNAL_SERVER_ERROR}

    return inner
