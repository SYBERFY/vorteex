import requests

from . import settings


class API:
    def __init__(self, authorization, sources):
        self.authorization = authorization
        self.sources = sources

    def get_global_module_map(self):
        response = requests.get(f'{settings.VORTEEX_BASE_URL}/get-global-map')

        if response.status_code != 200:
            raise Exception('Could not fetch global module map')

        return response.json()

    def make_query(self, source, resource, value):
        response = requests.post(
            url=f'{settings.VORTEEX_BASE_URL}/query',
            json={
                'source': source,
                'resource': resource,
                'value': value,
                'api_key': self.sources.get(source)
            }
        )

        if response.status_code != 200:
            print(response.text)
            return False

        return response.json().get('data')
