from blockscan.enums.actions_enum import ActionsEnum as actions
from blockscan.enums.fields_enum import FieldsEnum as fields
from blockscan.enums.modules_enum import ModulesEnum as modules
from blockscan.modules.module import Module


class GasTracker(Module):
    @staticmethod
    def get_est_confirmation_time(gas_price: int) -> str:
        """Get the estimated time, in seconds, for a transaction to be
        confirmed on the blockchain.

        :param gas_price: the price paid per unit of gas, in wei
        :type gas_price: int

        :return: seconds (est) before confirmation
        :rtype: str
        """

        return (
            f"{fields.MODULE}"
            f"{modules.GASTRACKER}"
            f"{fields.ACTION}"
            f"{actions.GAS_ESTIMATE}"
            f"{fields.GAS_PRICE}"
            f"{gas_price}"
        )

    @staticmethod
    def get_gas_oracle() -> str:
        """Get the current Safe, Proposed and Fast gas prices.

        :return: Gas price in wei
        :rtype: str
        """

        return (
            f"{fields.MODULE}"
            f"{modules.GASTRACKER}"
            f"{fields.ACTION}"
            f"{actions.GAS_ORACLE}"
        )


class ProGasTracker(GasTracker):
    @staticmethod
    def get_daily_average_gas_price(
        start_date: str,
        end_date: str,
        sort: str,
    ) -> str:
        """
        .. note:: Pro API token required

        Get the historical daily average gas price of the network
        within a date range

        :param start_date: the starting date in yyyy-MM-dd
        :type start_date: str
        :param end_date: the end date in yyyy-MM-dd
        :type end_date: str
        :param sort: the sorting preference (asc or desc)
        :type sort: str

        :return: daily average gas price
        :rtype: str
        """
        return (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_AVG_GAS_PRICE}"
            f"{fields.START_DATE}"
            f"{start_date}"
            f"{fields.END_DATE}"
            f"{end_date}"
            f"{fields.SORT}"
            f"{sort}"
        )

    @staticmethod
    def get_daily_average_gas_limit(
        start_date: str,
        end_date: str,
        sort: str,
    ) -> str:
        """
        .. note:: Pro API token required

        Get the historical daily average gas limit of the network
        within a date range

        :param start_date: the starting date in yyyy-MM-dd
        :type start_date: str
        :param end_date: the end date in yyyy-MM-dd
        :type end_date: str
        :param sort: the sorting preference (asc or desc)
        :type sort: str

        :return: daily average gas limit
        :rtype: str
        """
        return (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_AVG_GAS_LIMIT}"
            f"{fields.START_DATE}"
            f"{start_date}"
            f"{fields.END_DATE}"
            f"{end_date}"
            f"{fields.SORT}"
            f"{sort}"
        )

    @staticmethod
    def get_daily_total_gas_used(
        start_date: str,
        end_date: str,
        sort: str,
    ) -> str:
        """
        .. note:: Pro API token required

        Get the total amount of gas used daily for transactions on the network
        within a date range

        :param start_date: the starting date in yyyy-MM-dd
        :type start_date: str
        :param end_date: the end date in yyyy-MM-dd
        :type end_date: str
        :param sort: the sorting preference (asc or desc)
        :type sort: str

        :return: daily total gas used
        :rtype: str
        """
        return (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_GAS_USED}"
            f"{fields.START_DATE}"
            f"{start_date}"
            f"{fields.END_DATE}"
            f"{end_date}"
            f"{fields.SORT}"
            f"{sort}"
        )
