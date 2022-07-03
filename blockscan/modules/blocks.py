from blockscan.enums.actions_enum import ActionsEnum as actions
from blockscan.enums.fields_enum import FieldsEnum as fields
from blockscan.enums.modules_enum import ModulesEnum as modules
from blockscan.modules.module import Module


class Blocks(Module):
    """ """

    @staticmethod
    def get_block_reward_by_block_number(block_no: int):
        """Get block reward by block number.

        :param block_no: Target block number.
        :type block_no: int

        :returns: Block reward as a dictionary of various data.
        :rtype: dict

        """
        return (
            f"{fields.MODULE}"
            f"{modules.BLOCK}"
            f"{fields.ACTION}"
            f"{actions.GET_BLOCK_REWARD}"
            f"{fields.BLOCKNO}"
            f"{block_no}"
        )

    @staticmethod
    def get_est_block_countdown_time_by_block_number(block_no: int):
        """Get estimated countdown time for a given block.

        :param block_no: Target block number.
        :type block_no: int

        :returns: Countdown time in a dictionary of various data.
        :rtype: dict

        """
        return (
            f"{fields.MODULE}"
            f"{modules.BLOCK}"
            f"{fields.ACTION}"
            f"{actions.GET_BLOCK_COUNTDOWN}"
            f"{fields.BLOCKNO}"
            f"{block_no}"
        )

    @staticmethod
    def get_block_number_by_timestamp(timestamp: int, closest: str):
        """Get block number given a specific timestamp.

        .. note:: Supports UNIX timestamps in seconds.

        :param timestamp: Target timestamp.
        :type timestamp: int
        :param closest: Closest block "before" or "after" target timestamp.
        :type closest: str

        :returns: Block number for requested timestamp.
        :rtype: str

        """
        assert closest in ["before", "after"], "Specify 'before' or 'after'."
        return (
            f"{fields.MODULE}"
            f"{modules.BLOCK}"
            f"{fields.ACTION}"
            f"{actions.GET_BLOCK_NUMBER_BY_TIME}"
            f"{fields.TIMESTAMP}"
            f"{timestamp}"
            f"{fields.CLOSEST}"
            f"{closest}"
        )


class ProBlocks(Blocks):
    @staticmethod
    def get_daily_average_block_size(
        start_date: str,
        end_date: str,
        sort: str,
    ) -> str:
        """
        .. note:: Pro API token required

        Returns the daily average block size within a date range

        :param start_date: the starting date in yyyy-MM-dd
        :type start_date: str
        :param end_date: the end date in yyyy-MM-dd
        :type end_date: str
        :param sort: the sorting preference (asc or desc)
        :type sort: str

        :return: Daily average block size
        :rtype: str
        """
        return (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_AVG_BLOCK_SIZE}"
            f"{fields.START_DATE}"
            f"{start_date}"
            f"{fields.END_DATE}"
            f"{end_date}"
            f"{fields.SORT}"
            f"{sort}"
        )

    @staticmethod
    def get_daily_block_count_and_rewards(
        start_date: str,
        end_date: str,
        sort: str,
    ) -> str:
        """
        .. note:: Pro API token required

        Returns the number of blocks mined daily and the amount of block rewards
        within a date range

        :param start_date: the starting date in yyyy-MM-dd
        :type start_date: str
        :param end_date: the end date in yyyy-MM-dd
        :type end_date: str
        :param sort: the sorting preference (asc or desc)
        :type sort: str

        :return: daily mined block and reward
        :rtype: str
        """
        return (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_BLK_COUNT}"
            f"{fields.START_DATE}"
            f"{start_date}"
            f"{fields.END_DATE}"
            f"{end_date}"
            f"{fields.SORT}"
            f"{sort}"
        )

    @staticmethod
    def get_daily_block_rewards(
        start_date: str,
        end_date: str,
        sort: str,
    ) -> str:
        """
        .. note:: Pro API token required

        Returns the amount of block rewards distributed to miners daily within
        a date range

        :param start_date: the starting date in yyyy-MM-dd
        :type start_date: str
        :param end_date: the end date in yyyy-MM-dd
        :type end_date: str
        :param sort: the sorting preference (asc or desc)
        :type sort: str

        :return: daily block rewards
        :rtype: str
        """
        return (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_BLOCK_REWARDS}"
            f"{fields.START_DATE}"
            f"{start_date}"
            f"{fields.END_DATE}"
            f"{end_date}"
            f"{fields.SORT}"
            f"{sort}"
        )

    @staticmethod
    def get_daily_average_block_time(
        start_date: str,
        end_date: str,
        sort: str,
    ) -> str:
        """
        .. note:: Pro API token required

        Returns the daily average of time needed for a block to be successfully
        mined within a date range


        :param start_date: the starting date in yyyy-MM-dd
        :type start_date: str
        :param end_date: the end date in yyyy-MM-dd
        :type end_date: str
        :param sort: the sorting preference (asc or desc)
        :type sort: str

        :return: Daily average mining time
        :rtype: str
        """
        return (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_AVG_BLOCK_TIME}"
            f"{fields.START_DATE}"
            f"{start_date}"
            f"{fields.END_DATE}"
            f"{end_date}"
            f"{fields.SORT}"
            f"{sort}"
        )

    @staticmethod
    def get_daily_uncle_block_count_and_rewards(
        start_date: str,
        end_date: str,
        sort: str,
    ) -> str:
        """
        .. note:: Pro API token required

        Returns the number of 'Uncle' blocks mined daily and the amount of
        'Uncle' block rewards within a date range

        :param start_date: the starting date in yyyy-MM-dd
        :type start_date: str
        :param end_date: the end date in yyyy-MM-dd
        :type end_date: str
        :param sort: the sorting preference (asc or desc)
        :type sort: str

        :return: daily uncle blocks
        :rtype: str
        """
        return (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_UNCLE_BLK_COUNT}"
            f"{fields.START_DATE}"
            f"{start_date}"
            f"{fields.END_DATE}"
            f"{end_date}"
            f"{fields.SORT}"
            f"{sort}"
        )
