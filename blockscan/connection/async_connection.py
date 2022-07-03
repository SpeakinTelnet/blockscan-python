from typing import Dict, Optional
from functools import wraps
from blockscan.connection.base import BaseConnection
from blockscan.enums.fields_enum import FieldsEnum as fields
from blockscan.utils.request import async_get_response_from_get_request
from blockscan.modules import Module, get_default_modules, get_default_pro_modules
from blockscan.utils.parsing import ResponseParser as parser


class AsyncConnection(BaseConnection):
    is_async = True

    def __init__(
        self,
        chain_id: int,
        api_key: str,
        modules: Optional[Dict[str, Module]] = None,
        pro: bool = False,
        debug: bool = False,
    ) -> None:
        super().__init__(chain_id, api_key, debug=debug)
        if modules is None:
            modules = get_default_modules() if not pro else get_default_pro_modules()
        self.attach_decorated_module(modules, self.async_caller)

    def async_caller(self, func):
        """Decorator used as an async url call function that
        returns a formated response.
        """

        @wraps(func)
        async def wrapper(*args, **kwargs):
            url = (
                f"{self._prefix}"
                f"{func(*args, **kwargs)}"
                f"{fields.API_KEY}"
                f"{self._api_key}"
            )
            if self._debug:
                print(f"\n{url}\n")
            response = await async_get_response_from_get_request(url)
            return parser.parse(await response.json())

        return wrapper

    async def __aenter__(self):
        """Magic method for use in async with statement"""
        return self

    async def __aexit__(self, *args):
        """Magic method to close the async with statement session"""
        pass
