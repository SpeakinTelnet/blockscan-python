from collections import (
    OrderedDict,
)
import hashlib
import threading
from typing import (
    Any,
    Dict,
)

from aiohttp import (
    ClientResponse,
    ClientSession,
    ClientTimeout,
)
import lru
import requests


def generate_cache_key(value: str) -> str:
    """
    Generates a cache key for the *args and **kwargs
    """
    return hashlib.md5(value.encode("utf-8")).hexdigest()


class SessionCache:
    def __init__(self, size: int):
        self._size = size
        self._data: OrderedDict[str, Any] = OrderedDict()

    def cache(self, key: str, value: Any) -> Dict[str, Any]:
        evicted_items = None
        # If the key is already in the OrderedDict just update it
        # and don't evict any values. Ideally, we could still check to see
        # if there are too many items in the OrderedDict but that may rearrange
        # the order it should be unlikely that the size could grow over the limit
        if key not in self._data:
            while len(self._data) >= self._size:
                if evicted_items is None:
                    evicted_items = {}
                k, v = self._data.popitem(last=False)
                evicted_items[k] = v
        self._data[key] = value
        return evicted_items

    def get_cache_entry(self, key: str) -> Any:
        return self._data[key]

    def __contains__(self, item: str) -> bool:
        return item in self._data


def _remove_session(_key: str, session: requests.Session) -> None:
    session.close()


_session_cache = lru.LRU(8, callback=_remove_session)


def get_session(endpoint_uri: str) -> requests.Session:
    cache_key = generate_cache_key(endpoint_uri)
    if cache_key not in _session_cache:
        _session_cache[cache_key] = requests.Session()
    return _session_cache[cache_key]


def get_response_from_get_request(
    url: str, *args: Any, **kwargs: Any
) -> requests.Response:
    kwargs.setdefault("timeout", 10)
    session = get_session(url)
    response = session.get(url, *args, **kwargs)
    return response


# --- async --- #

_async_session_cache_lock = threading.Lock()
_async_session_cache = SessionCache(size=20)


async def cache_async_session(endpoint_uri, session: ClientSession) -> None:
    cache_key = generate_cache_key(endpoint_uri)
    with _async_session_cache_lock:
        evicted_items = _async_session_cache.cache(cache_key, session)
        if evicted_items is not None:
            for key, session in evicted_items.items():
                await session.close()


async def get_async_session(endpoint_uri) -> ClientSession:
    cache_key = generate_cache_key(endpoint_uri)
    if cache_key not in _async_session_cache:
        await cache_async_session(endpoint_uri, ClientSession(raise_for_status=True))
    return _async_session_cache.get_cache_entry(cache_key)


async def async_get_response_from_get_request(
    endpoint_uri, *args: Any, **kwargs: Any
) -> ClientResponse:
    kwargs.setdefault("timeout", ClientTimeout(10))
    session = await get_async_session(endpoint_uri)
    response = await session.get(endpoint_uri, *args, **kwargs)
    return response
