from typing import Dict, Optional
from blockscan.modules import Module
from blockscan.connection.base import BaseConnection
from blockscan.connection.sync_connection import SyncConnection
from blockscan.connection.async_connection import AsyncConnection


class Blockscan:
    """Create a new client with the provided modules

    :param chain_id: The specific blockchain ID (i.e Polygonscan == 137)
    :type chain_id: int
    :param api_key: Your blockscan API KEY (blockchain specific)
    :type api_key: str
    :param is_async: Whether you want an async client or not, defaults to True
    :type is_async: bool, optional
    :param modules: Modules to be attached to the client,
            if none is provided it will fetch all.
            Formated as ``{"module": Module}``
    :type modules: Optional[Dict[str, Module]], optional
    :param debug: Display generated URLs for debugging, defaults to False
    :type debug: bool, optional
    :param pro: Also attach the Pro modules to the client. Overwritten if
            modules are manually provided, default to False
    :type pro: bool, optional
    :param testing: apply only to sync, will return the json data necessary
                    for the unittests, use only for developping purpose.
                    defaults to False
    :type testing: bool, optional
    :return: A connection client
    :rtype: BaseConnection

    """

    def __new__(
        cls,
        chain_id: int,
        api_key: str,
        is_async: bool = True,
        modules: Optional[Dict[str, Module]] = None,
        debug: bool = False,
        pro: bool = False,
        testing: bool = False,
    ) -> BaseConnection:

        if is_async:
            return AsyncConnection(
                chain_id, api_key, modules=modules, pro=pro, debug=debug
            )
        return SyncConnection(
            chain_id, api_key, modules=modules, pro=pro, debug=debug, testing=testing
        )
