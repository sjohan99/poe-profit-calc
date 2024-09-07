import json
import pathlib
from typing import Union
import requests
from cachetools import TTLCache, LRUCache, cached


class FetchError(Exception):
    pass


class HttpFetcher:
    def __init__(self, headers=None):
        self.session = requests.Session()
        if headers:
            self.session.headers.update(headers)

    @cached(cache=TTLCache(maxsize=8196, ttl=1800))
    def fetch_data(self, url):
        response = self.session.get(url)
        try:
            response.raise_for_status()
        except requests.RequestException as e:
            raise FetchError(
                f"HttpFetcher: Failed to fetch data from {url} with message: {str(e)}"
            ) from e
        return response.json()


class FileFetcher:
    @cached(cache=LRUCache(maxsize=256))
    def fetch_data(self, path):
        file = pathlib.Path(path)
        try:
            with open(file, "r") as f:
                return json.loads(f.read())
        except FileNotFoundError as e:
            raise FetchError(
                f"FileFetcher: Failed to fetch data from {path} with message: {str(e)}"
            ) from e


Fetcher = Union[HttpFetcher, FileFetcher]
