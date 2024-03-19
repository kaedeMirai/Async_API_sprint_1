import logging
from glob import glob

import pytest_asyncio
import asyncio

from tests.functional.fixtures.es_fixtures import *
from tests.functional.fixtures.redis_fixtures import *
from tests.functional.fixtures.http_request_fixtures import *

pytest_plugins = [
    fixture_file.replace("/", ".").replace(".py", "")
    for fixture_file in glob(
        "/fixtures/[!__]*.py",
        recursive=True
    )
]

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest_asyncio.fixture(scope='session')
def event_loop(request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(asyncio.sleep(0))
    yield loop
    loop.close()




