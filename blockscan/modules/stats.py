from blockscan.enums.actions_enum import ActionsEnum as actions
from blockscan.enums.fields_enum import FieldsEnum as fields
from blockscan.enums.modules_enum import ModulesEnum as modules
from blockscan.modules.module import Module


class Stats(Module):
    """ """

    def __init__(self, parent_connection) -> None:
        super().__init__()
        self.supply = parent_connection._supply
        self.price = parent_connection._price
        self.daily_price = parent_connection._daily_price
        self.daily_market_cap = parent_connection._daily_market_cap

    def get_total_currency_supply(self):
        """Get total supply of main currency on selected chain.


        :returns: The total supply of currency.
        :rtype: str

        """
        return f"{fields.MODULE}" f"{modules.STATS}" f"{fields.ACTION}" f"{self.supply}"

    def get_total_eth2_supply(self):
        """Get total supply of ETH2 currency.


        :returns: The total supply of ETH2.
        :rtype: str

        """
        return (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.ETH2_SUPPLY}"
        )

    def get_currency_last_price(self):
        """Get the last price of the main currency against BTC and USD.


        :returns: Latest dictionary of currency price pairs.
        :rtype: dict

        """
        return f"{fields.MODULE}" f"{modules.STATS}" f"{fields.ACTION}" f"{self.price}"

    def get_validators_list(self):
        """Get list of validators on POE network.


        :returns: All validators as a list of dictionaries.
        :rtype: List[dict]

        """
        return (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.VALIDATORS}"
        )

    def get_nodes_size(
        self,
        start_date: str,
        end_date: str,
        client_type: str,
        sync_mode: str,
        sort: str,
    ) -> str:
        """Get the size of the blockchain, in bytes, over a date range.

        :param start_date: the starting date in yyyy-MM-dd
        :type start_date: str
        :param end_date: the end date in yyyy-MM-dd
        :type end_date: str
        :param client_type: The node client to use (i.e geth or parity)
        :type client_type: str
        :param sync_mode: type of node, default or archive
        :type sync_mode: str
        :param sort: the sorting preference (asc or desc)
        :type sort: str

        :return: blockchain size
        :rtype: str
        """

        return (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.CHAIN_SIZE}"
            f"{fields.START_DATE}"
            f"{start_date}"
            f"{fields.END_DATE}"
            f"{end_date}"
            f"{fields.CLIENT_TYPE}"
            f"{client_type}"
            f"{fields.SYNC_MODE}"
            f"{sync_mode}"
            f"{fields.SORT}"
            f"{sort}"
        )


class ProStats(Stats):
    def get_eth_daily_network_tx_fee(
        self,
        start_date: str,
        end_date: str,
        sort: str,
    ) -> str:
        """
        .. note:: Pro API token required

        Get the amount of transaction fees paid to miners per day
        within a date range

        :param start_date: the starting date in yyyy-MM-dd
        :type start_date: str
        :param end_date: the end date in yyyy-MM-dd
        :type end_date: str
        :param sort: the sorting preference (asc or desc)
        :type sort: str

        :return: Transaction fees paid
        :rtype: str
        """
        return (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_TXN_FEE}"
            f"{fields.START_DATE}"
            f"{start_date}"
            f"{fields.END_DATE}"
            f"{end_date}"
            f"{fields.SORT}"
            f"{sort}"
        )

    def get_daily_new_address_count(
        self,
        start_date: str,
        end_date: str,
        sort: str,
    ) -> str:
        """
        .. note:: Pro API token required

        Get the number of new addresses created per day
        within a date range

        :param start_date: the starting date in yyyy-MM-dd
        :type start_date: str
        :param end_date: the end date in yyyy-MM-dd
        :type end_date: str
        :param sort: the sorting preference (asc or desc)
        :type sort: str

        :return: daily new address
        :rtype: str
        """
        return (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_NEW_ADDRESS}"
            f"{fields.START_DATE}"
            f"{start_date}"
            f"{fields.END_DATE}"
            f"{end_date}"
            f"{fields.SORT}"
            f"{sort}"
        )

    def get_daily_network_utilization(
        self,
        start_date: str,
        end_date: str,
        sort: str,
    ) -> str:
        """
        .. note:: Pro API token required

        Get the daily average gas used over gas limit, in percentage
        within a date range

        :param start_date: the starting date in yyyy-MM-dd
        :type start_date: str
        :param end_date: the end date in yyyy-MM-dd
        :type end_date: str
        :param sort: the sorting preference (asc or desc)
        :type sort: str

        :return: daily average gas used over gas limit
        :rtype: str
        """
        return (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_NET_UTILIZATION}"
            f"{fields.START_DATE}"
            f"{start_date}"
            f"{fields.END_DATE}"
            f"{end_date}"
            f"{fields.SORT}"
            f"{sort}"
        )

    def get_daily_average_network_hash_rate(
        self,
        start_date: str,
        end_date: str,
        sort: str,
    ) -> str:
        """
        .. note:: Pro API token required

        Get the historical measure of processing power of the network
        within a date range

        :param start_date: the starting date in yyyy-MM-dd
        :type start_date: str
        :param end_date: the end date in yyyy-MM-dd
        :type end_date: str
        :param sort: the sorting preference (asc or desc)
        :type sort: str

        :return: daily hashrate
        :rtype: str
        """
        return (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_AVG_HASH_RATE}"
            f"{fields.START_DATE}"
            f"{start_date}"
            f"{fields.END_DATE}"
            f"{end_date}"
            f"{fields.SORT}"
            f"{sort}"
        )

    def get_daily_tx_count(
        self,
        start_date: str,
        end_date: str,
        sort: str,
    ) -> str:
        """
        .. note:: Pro API token required

        Get the number of transactions performed on the blockchain per day
        within a date range

        :param start_date: the starting date in yyyy-MM-dd
        :type start_date: str
        :param end_date: the end date in yyyy-MM-dd
        :type end_date: str
        :param sort: the sorting preference (asc or desc)
        :type sort: str

        :return: number of transactions
        :rtype: str
        """
        return (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_TX}"
            f"{fields.START_DATE}"
            f"{start_date}"
            f"{fields.END_DATE}"
            f"{end_date}"
            f"{fields.SORT}"
            f"{sort}"
        )

    def get_daily_average_network_difficulty(
        self,
        start_date: str,
        end_date: str,
        sort: str,
    ) -> str:
        """
        .. note:: Pro API token required

        Get the historical mining difficulty of the network
        within a date range

        :param start_date: the starting date in yyyy-MM-dd
        :type start_date: str
        :param end_date: the end date in yyyy-MM-dd
        :type end_date: str
        :param sort: the sorting preference (asc or desc)
        :type sort: str

        :return: daily mining difficulty
        :rtype: str
        """
        return (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_AVG_NET_DIFFICULTY}"
            f"{fields.START_DATE}"
            f"{start_date}"
            f"{fields.END_DATE}"
            f"{end_date}"
            f"{fields.SORT}"
            f"{sort}"
        )

    def get_hist_daily_market_cap(
        self,
        start_date: str,
        end_date: str,
        sort: str,
    ) -> str:
        """
        .. note:: Pro API token required

        Get the historical daily market capitalization
        within a date range

        :param start_date: the starting date in yyyy-MM-dd
        :type start_date: str
        :param end_date: the end date in yyyy-MM-dd
        :type end_date: str
        :param sort: the sorting preference (asc or desc)
        :type sort: str

        :return: daily market capitalization
        :rtype: str
        """
        return (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{self.daily_market_cap}"
            f"{fields.START_DATE}"
            f"{start_date}"
            f"{fields.END_DATE}"
            f"{end_date}"
            f"{fields.SORT}"
            f"{sort}"
        )

    def get_eth_hist_price(
        self,
        start_date: str,
        end_date: str,
        sort: str,
    ) -> str:
        """
        .. note:: Pro API token required

        Get the historical price of 1 unit of the currency
        within a date range

        :param start_date: the starting date in yyyy-MM-dd
        :type start_date: str
        :param end_date: the end date in yyyy-MM-dd
        :type end_date: str
        :param sort: the sorting preference (asc or desc)
        :type sort: str

        :return: daily price
        :rtype: str
        """
        return (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{self.daily_price}"
            f"{fields.START_DATE}"
            f"{start_date}"
            f"{fields.END_DATE}"
            f"{end_date}"
            f"{fields.SORT}"
            f"{sort}"
        )
