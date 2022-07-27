from typing import Dict, Callable
from blockscan.modules import (
    Module,
    ProAccounts,
    ProBlocks,
    ProContracts,
    ProLogs,
    ProProxy,
    ProStats,
    ProTokens,
    ProTransactions,
    ProGasTracker,
)
from blockscan.blockchains import blockchains
from blockscan.exception import ChainIDError


class BaseConnection:
    """Base connection class"""

    accounts = ProAccounts
    blocks = ProBlocks
    contracts = ProContracts
    logs = ProLogs
    proxy = ProProxy
    stats = ProStats
    tokens = ProTokens
    transactions = ProTransactions
    gas_tracker = ProGasTracker

    def __init__(
        self,
        chain_id: int,
        api_key: str,
        debug: bool = False,  # display generated URLs for debugging purposes
    ):
        try:
            blockchain = blockchains[chain_id]
        except KeyError:
            raise ChainIDError(f"Chain ID {chain_id} not recognized")

        self._prefix = blockchain["url"]
        self._price = blockchain["price"]
        self._supply = blockchain["supply"]
        self._daily_price = blockchain["daily_price"]
        self._daily_market_cap = blockchain["daily_market_cap"]
        self._api_key = api_key
        self._debug = debug

    def attach_decorated_module(self, modules: Dict[str, Module], decorator: Callable):
        """Attach the supplied module(s) to self with a custom
        decorator for the included functions

        :param modules: Dict of modules to be attached
        :type modules: Dict[str, Module]
        :param decorator: Decorator to be used on the modules functions
        :type decorator: Callable
        """
        for module_name, module_info in modules.items():
            if module_name == "stats":
                module_info = module_info(self)
                module_info._add_decorator(decorator)
            else:
                module_info._add_decorator(decorator)
            setattr(self, module_name, module_info)
