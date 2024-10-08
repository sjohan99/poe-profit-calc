from enum import Enum
import json
import pathlib
import requests
from cachetools import TTLCache, LRUCache, cached


class FetchError(Exception):
    pass


class Format(Enum):
    JSON = "json"
    BYTES = "bytes"


class HttpFetcher:
    def __init__(self, headers=None):
        self.session = requests.Session()
        if headers:
            self.session.headers.update(headers)

    @cached(cache=TTLCache(maxsize=8196, ttl=1800))
    def fetch_data(self, url, format: Format = Format.JSON):
        response = self.session.get(url)
        try:
            response.raise_for_status()
        except requests.RequestException as e:
            raise FetchError(
                f"HttpFetcher: Failed to fetch data from {url} with message: {str(e)}"
            ) from e
        if format == Format.BYTES:
            return response.content
        return response.json()


class FileFetcher:
    @cached(cache=LRUCache(maxsize=256))
    def fetch_data(self, path, format: Format = Format.JSON):
        file = pathlib.Path(path)
        try:
            if format == Format.BYTES:
                with open(file, "rb") as f:
                    return f.read()
            with open(file, "r") as f:
                return json.loads(f.read())
        except FileNotFoundError as e:
            raise FetchError(
                f"FileFetcher: Failed to fetch data from {path} with message: {str(e)}"
            ) from e


Fetcher = HttpFetcher | FileFetcher
