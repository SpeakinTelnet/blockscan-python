from functools import reduce
from typing import List

from blockscan.enums.actions_enum import ActionsEnum as actions
from blockscan.enums.fields_enum import FieldsEnum as fields
from blockscan.enums.modules_enum import ModulesEnum as modules
from blockscan.enums.tags_enum import TagsEnum as tags
from blockscan.modules.module import Module


class Accounts(Module):
    """ """

    @staticmethod
    def get_currency_balance(address: str):
        """Get the Currency balance of an account.

        :param address: Target account.
        :type address: str

        :returns: Its balance as a string. Must be manually cast to float.
        :rtype: str

        """

        return (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.BALANCE}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.TAG}"
            f"{tags.LATEST}"
        )

    @staticmethod
    def get_currency_balance_multiple(addresses: List[str]):
        """Get the currency balance of multiple accounts.

        .. note:: Max 20 accounts per call are supported.**

        :param addresses: List of target accounts.
        :type addresses: List[str]

        :returns: Their balances in a list of dictionaries.
        :rtype: List[dict]

        """
        address_list = reduce(lambda w1, w2: str(w1) + "," + str(w2), addresses)
        return (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.BALANCE_MULTI}"
            f"{fields.ADDRESS}"
            f"{address_list}"
            f"{fields.TAG}"
            f"{tags.LATEST}"
        )

    @staticmethod
    def get_normal_txs_by_address(
        address: str,
        startblock: int,
        endblock: int,
        sort: str,
    ):
        """Get a list of all normal transactions for an address.

        .. note:: Returns the 10,000 most recent transactions.

        :param address: Target address.
        :type address: str
        :param startblock: Start block of the query.
        :type startblock: int
        :param endblock: End block of the query.
        :type endblock: int
        :param sort: "asc" to return results in ascending order.
        :type sort: str

        :returns: A list of dictionaries of normal transactions.
        :rtype: List[dict]

        """
        return (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TXLIST}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.START_BLOCK}"
            f"{str(startblock)}"
            f"{fields.END_BLOCK}"
            f"{str(endblock)}"
            f"{fields.SORT}"
            f"{sort}"
        )

    @staticmethod
    def get_normal_txs_by_address_paginated(
        address: str,
        page: int,
        offset: int,
        startblock: int,
        endblock: int,
        sort: str,
    ):
        """Get a list of all normal transactions for an address as numbered pages.

        :param address: Target address.
        :type address: str
        :param page: Page number to fetch.
        :type page: int
        :param offset: Max records to return.
        :type offset: int
        :param startblock: Start block of the query.
        :type startblock: int
        :param endblock: End block of the query.
        :type endblock: int
        :param sort: "asc" to return results in ascending order.
        :type sort: str

        :returns: All transactions on requested page as a list of dictionaries.
        :rtype: List[dict]

        """
        return (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TXLIST}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.START_BLOCK}"
            f"{str(startblock)}"
            f"{fields.END_BLOCK}"
            f"{str(endblock)}"
            f"{fields.SORT}"
            f"{sort}"
            f"{fields.PAGE}"
            f"{str(page)}"
            f"{fields.OFFSET}"
            f"{str(offset)}"
        )

    @staticmethod
    def get_internal_txs_by_address(
        address: str,
        startblock: int,
        endblock: int,
        sort: str,
    ):
        """Get a list of all internal transactions for an address.

        .. note:: Returns the 10,000 most recent transactions.

        :param address: Target address.
        :type address: str
        :param startblock: Start block of the query.
        :type startblock: int
        :param endblock: End block of the query.
        :type endblock: int
        :param sort: "asc" to return results in ascending order.
        :type sort: str

        :returns: A list of dictionaries of internal transactions.
        :rtype: List[dict]

        """
        return (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TXLIST_INTERNAL}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.START_BLOCK}"
            f"{str(startblock)}"
            f"{fields.END_BLOCK}"
            f"{str(endblock)}"
            f"{fields.SORT}"
            f"{sort}"
        )

    @staticmethod
    def get_internal_txs_by_address_paginated(
        address: str,
        page: int,
        offset: int,
        startblock: int,
        endblock: int,
        sort: str,
    ):
        """Get a list of all internal transactions for an address as numbered pages.

        :param address: Target address.
        :type address: str
        :param page: Page number to fetch.
        :type page: int
        :param offset: Max records to return.
        :type offset: int
        :param startblock: Start block of the query.
        :type startblock: int
        :param endblock: End block of the query.
        :type endblock: int
        :param sort: "asc" to return results in ascending order.
        :type sort: str

        :returns: All transactions on requested page as a list of dictionaries.
        :rtype: List[dict]

        """
        return (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TXLIST_INTERNAL}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.START_BLOCK}"
            f"{str(startblock)}"
            f"{fields.END_BLOCK}"
            f"{str(endblock)}"
            f"{fields.SORT}"
            f"{sort}"
            f"{fields.PAGE}"
            f"{str(page)}"
            f"{fields.OFFSET}"
            f"{str(offset)}"
        )

    @staticmethod
    def get_internal_txs_by_txhash(txhash: str):
        """Get all internal transactions given for a tx hash.

        .. note:: Returns the 10,000 most recent transactions.

        :param txhash: Target tx hash.
        :type txhash: str

        :returns: All internal transactions as a list of dictionaries.
        :rtype: List[dict]

        """
        return (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TXLIST_INTERNAL}"
            f"{fields.TXHASH}"
            f"{txhash}"
        )

    @staticmethod
    def get_internal_txs_by_block_range_paginated(
        startblock: int,
        endblock: int,
        page: int,
        offset: int,
        sort: str,
    ):
        """Get all internal transactions given for a
        given block range as numbered pages.

        .. note:: Returns the 10,000 most recent transactions.

        :param startblock: Start block of the query.
        :type startblock: int
        :param endblock: End block of the query.
        :type endblock: int
        :param page: Page number to fetch.
        :type page: int
        :param offset: Max records to return.
        :type offset: int
        :param sort: "asc" to return results in ascending order.
        :type sort: str

        :returns: All internal transactions as a list of dictionaries.
        :rtype: List[dict]

        """
        return (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TXLIST_INTERNAL}"
            f"{fields.START_BLOCK}"
            f"{str(startblock)}"
            f"{fields.END_BLOCK}"
            f"{str(endblock)}"
            f"{fields.SORT}"
            f"{sort}"
            f"{fields.PAGE}"
            f"{str(page)}"
            f"{fields.OFFSET}"
            f"{str(offset)}"
        )

    @staticmethod
    def get_tokentx_token_transfer_events_by_address(
        address: str,
        startblock: int,
        endblock: int,
        sort: str,
    ):
        """Get all BEP20 token transfer events for a given address.

        .. note:: Returns the 10,000 most recent events.

        :param address: Target address.
        :type address: str
        :param startblock: Start block of the query.
        :type startblock: int
        :param endblock: End block of the query.
        :type endblock: int
        :param sort: "asc" to return results in ascending order.
        :type sort: str

        :returns: All token transfers for target address.
        :rtype: List[dict]

        """

        return (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TOKENTX}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.START_BLOCK}"
            f"{str(startblock)}"
            f"{fields.END_BLOCK}"
            f"{str(endblock)}"
            f"{fields.SORT}"
            f"{sort}"
        )

    @staticmethod
    def get_tokentx_token_transfer_events_by_contract_address_paginated(
        contract_address: str, page: int, offset: int, sort: str
    ):
        """Get all token transfer events for a given BEP20 contract as numbered pages.

        .. note:: Returns the 10,000 most recent events.

        :param contract_address: Target contract address.
        :type contract_address: str
        :param page: Page number to fetch.
        :type page: int
        :param offset: Max records to return.
        :type offset: int
        :param sort: "asc" to return results in ascending order.
        :type sort: str

        :returns: All token transfers for target contract address.
        :rtype: List[dict]

        """
        return (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TOKENTX}"
            f"{fields.CONTRACT_ADDRESS}"
            f"{contract_address}"
            f"{fields.SORT}"
            f"{sort}"
            f"{fields.PAGE}"
            f"{str(page)}"
            f"{fields.OFFSET}"
            f"{str(offset)}"
        )

    @staticmethod
    def get_tokentx_token_transfer_events_by_address_and_contract_paginated(
        contract_address: str, address: str, page: int, offset: int, sort: str
    ):
        """Get all token transfers for a given BEP20
        contract and wallet as numbered pages.

        :param contract_address: Target contract address.
        :type contract_address: str
        :param address: Target wallet address.
        :type address: str
        :param page: Page number to fetch.
        :type page: int
        :param offset: Max records to return.
        :type offset: int
        :param sort: "asc" to return results in ascending order.
        :type sort: str

        :returns: All token transfers as a list of dictionaries.
        :rtype: List[dict]

        """

        return (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TOKENTX}"
            f"{fields.CONTRACT_ADDRESS}"
            f"{contract_address}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.SORT}"
            f"{sort}"
            f"{fields.PAGE}"
            f"{str(page)}"
            f"{fields.OFFSET}"
            f"{str(offset)}"
        )

    @staticmethod
    def get_nfttx_token_transfer_events_by_address(
        address: str,
        startblock: int,
        endblock: int,
        sort: str,
    ):
        """Get all BEP721 token transfer events for a given address.

        .. note:: Returns the 10,000 most recent events.

        :param address: Target address.
        :type address: str
        :param startblock: Start block of the query.
        :type startblock: int
        :param endblock: End block of the query.
        :type endblock: int
        :param sort: "asc" to return results in ascending order.
        :type sort: str

        :returns: All token transfers for target address.
        :rtype: List[dict]

        """
        return (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TOKENNFTTX}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.START_BLOCK}"
            f"{str(startblock)}"
            f"{fields.END_BLOCK}"
            f"{str(endblock)}"
            f"{fields.SORT}"
            f"{sort}"
        )

    @staticmethod
    def get_nfttx_token_transfer_events_by_contract_address_paginated(
        contract_address: str, page: int, offset: int, sort: str
    ):
        """Get all token transfer events for a given BEP721 contract as numbered pages.

        .. note:: Returns the 10,000 most recent events.

        :param contract_address: Target contract address.
        :type contract_address: str
        :param page: Page number to fetch.
        :type page: int
        :param offset: Max records to return.
        :type offset: int
        :param sort: "asc" to return results in ascending order.
        :type sort: str

        :returns: All token transfers for target contract address.
        :rtype: List[dict]

        """
        return (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TOKENNFTTX}"
            f"{fields.CONTRACT_ADDRESS}"
            f"{contract_address}"
            f"{fields.SORT}"
            f"{sort}"
            f"{fields.PAGE}"
            f"{str(page)}"
            f"{fields.OFFSET}"
            f"{str(offset)}"
        )

    @staticmethod
    def get_nfttx_token_transfer_events_by_address_and_contract_paginated(
        contract_address: str, address: str, page: int, offset: int, sort: str
    ):
        """Get all token transfers for a given BEP721
        contract and wallet as numbered pages.

        :param contract_address: Target contract address.
        :type contract_address: str
        :param address: Target wallet address.
        :type address: str
        :param page: Page number to fetch.
        :type page: int
        :param offset: Max records to return.
        :type offset: int
        :param sort: "asc" to return results in ascending order.
        :type sort: str

        :returns: All token transfers as a list of dictionaries.
        :rtype: List[dict]

        """
        return (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TOKENNFTTX}"
            f"{fields.CONTRACT_ADDRESS}"
            f"{contract_address}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.SORT}"
            f"{sort}"
            f"{fields.PAGE}"
            f"{str(page)}"
            f"{fields.OFFSET}"
            f"{str(offset)}"
        )

    @staticmethod
    def get_mined_blocks_by_address(address: str):
        """Get a list of validated blocks by a specific address.

        :param address: Target validator address.
        :type address: str

        :returns: All validated blocks as a list of dictionaries.
        :rtype: List[dict]

        """
        return (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.GET_MINED_BLOCKS}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.BLOCK_TYPE}"
            f"{fields.BLOCKS}"
        )

    @staticmethod
    def get_mined_blocks_by_address_paginated(address: str, page: int, offset: int):
        """Get a list of validated blocks by a specific address as numbered pages.

        :param address: Target validator address.
        :type address: str
        :param page: Page number to fetch.
        :type page: int
        :param offset: Max records to return.
        :type offset: int

        :returns: All validated blocks as list of dictionaries per page.
        :rtype: List[dict]

        """
        return (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.GET_MINED_BLOCKS}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.BLOCK_TYPE}"
            f"{fields.BLOCKS}"
            f"{fields.PAGE}"
            f"{str(page)}"
            f"{fields.OFFSET}"
            f"{str(offset)}"
        )


class ProAccounts(Accounts):
    @staticmethod
    def get_hist_eth_balance_for_address_by_block_no(
        address: str, block_no: int
    ) -> str:
        """
        .. note:: Pro API token required

        Returns the balance of an address at a certain block height.

        :param address: the string representing the address to check for balance
        :type address: str
        :param block_no: the block number to check balance for
        :type block_no: int

        :return: address balance
        :rtype: str
        """
        return (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.BALANCE_HISTORY}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.BLOCKNO}"
            f"{block_no}"
        )
