from functools import wraps
from blockscan.utils.request import get_response_from_get_request
from blockscan.utils.parsing import ResponseParser as parser
from blockscan.enums.fields_enum import FieldsEnum as fields


def sync_caller(func):
    """Decorator used as a url call function that returns
    a formated response.
    """

    @wraps(func)
    def wrapper(self, *args, **kwargs):
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
