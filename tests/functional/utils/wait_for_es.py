from elasticsearch import Elasticsearch

from settings import test_settings
from helpers import backoff, ConnectionException


@backoff((ConnectionException,))
def wait_for_es(client):
    if not client.ping():
        raise ConnectionException('ES client is not ready yet')


if __name__ == '__main__':
    host = f'{test_settings.es_host}:{test_settings.es_port}'
    es_client = Elasticsearch(hosts=host, validate_cert=False, use_ssl=False)

    wait_for_es(es_client)
