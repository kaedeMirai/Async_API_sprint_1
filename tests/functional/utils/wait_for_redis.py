from redis import Redis

from settings import test_settings
from helpers import backoff, ConnectionException


@backoff((ConnectionException,))
def wait_for_redis(client):
    if not client.ping():
        raise ConnectionException('Redis client is not ready yet')


if __name__ == '__main__':
    redis_client = Redis(host=test_settings.redis_host, port=test_settings.redis_port, db=0)
    wait_for_redis(redis_client)
