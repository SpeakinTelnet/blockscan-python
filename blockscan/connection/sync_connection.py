from functools import wraps
from typing import Dict, Optional
import json
from blockscan.connection.base import BaseConnection
from blockscan.utils.request import get_response_from_get_request
from blockscan.enums.fields_enum import FieldsEnum as fields
from blockscan.modules import Module, get_default_modules, get_default_pro_modules
from blockscan.utils.parsing import ResponseParser as parser


class SyncConnection(BaseConnection):

    is_async = False

    def __init__(
        self,
        chain_id: int,
        api_key: str,
        modules: Optional[Dict[str, Module]] = None,
        pro: bool = False,
        debug: bool = False,
        testing: bool = False,
    ) -> None:
        super().__init__(chain_id, api_key, debug=debug)
        if modules is None:
            modules = get_default_modules() if not pro else get_default_pro_modules()
        if testing:
            self.attach_decorated_module(modules, self.sync_test_caller)
        else:
            self.attach_decorated_module(modules, self.sync_caller)

    def sync_caller(self, func):
        """Decorator used as a url call function that returns
        a formated response.
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            url = (
                f"{self._prefix}"
                f"{func(*args, **kwargs)}"
                f"{fields.API_KEY}"
                f"{self._api_key}"
            )
            if self._debug:
                print(f"\n{url}\n")
            response = get_response_from_get_request(url)
            # with self._session.get(url) as response:
            return parser.parse(response.json())

        return wrapper

    def sync_test_caller(self, func):
        """Decorator used as a url call function that returns
        a formated response.
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            url = (
                f"{self._prefix}"
                f"{func(*args, **kwargs)}"
                f"{fields.API_KEY}"
                f"{self._api_key}"
            )
            sterilized_url = (
                f"https://api.test.io/api?"
                f"{func(*args, **kwargs)}"
                f"{fields.API_KEY}"
                "TEST"
            )
            response = get_response_from_get_request(url)
            assertion = parser.parse(response.json())
            test_response = {
                str(func.__name__): {
                    "url": sterilized_url,
                    "kwargs": kwargs,
                    "response": response.json(),
                    "assertion": assertion,
                }
            }
            return json.dumps(test_response, indent=4)

        return wrapper

    def __enter__(self):
        """Magic method for use in with statement"""
        return self

    def __exit__(self, *args):
        pass
