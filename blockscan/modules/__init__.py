from typing import Dict, Type

from blockscan.modules.accounts import Accounts, ProAccounts
from blockscan.modules.blocks import Blocks, ProBlocks
from blockscan.modules.contracts import Contracts, ProContracts
from blockscan.modules.gas_tracker import GasTracker, ProGasTracker
from blockscan.modules.logs import Logs, ProLogs
from blockscan.modules.proxy import Proxy, ProProxy
from blockscan.modules.stats import Stats, ProStats
from blockscan.modules.tokens import Tokens, ProTokens
from blockscan.modules.transactions import Transactions, ProTransactions
from blockscan.modules.module import Module


def get_default_modules() -> Dict[str, Type[Module]]:
    return {
        "accounts": Accounts,
        "blocks": Blocks,
        "contracts": Contracts,
        "logs": Logs,
        "proxy": Proxy,
        "stats": Stats,
        "tokens": Tokens,
        "transactions": Transactions,
        "gas_tracker": GasTracker,
    }


def get_default_pro_modules() -> Dict[str, Type[Module]]:
    return {
        "accounts": ProAccounts,
        "blocks": ProBlocks,
        "contracts": ProContracts,
        "logs": ProLogs,
        "proxy": ProProxy,
        "stats": ProStats,
        "tokens": ProTokens,
        "transactions": ProTransactions,
        "gas_tracker": ProGasTracker,
    }
