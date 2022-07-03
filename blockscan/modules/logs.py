from typing import Optional
from blockscan.enums.actions_enum import ActionsEnum as actions
from blockscan.enums.fields_enum import FieldsEnum as fields
from blockscan.enums.modules_enum import ModulesEnum as modules
from blockscan.modules.module import Module


class Logs(Module):
    @staticmethod
    def get_logs(
        from_block: int,
        to_block: int,
        address: str,
        topic_0: Optional[str] = None,
        topic_1: Optional[str] = None,
        topic_2: Optional[str] = None,
        topic_3: Optional[str] = None,
        topic_0_1_opr: Optional[str] = None,
        topic_1_2_opr: Optional[str] = None,
        topic_2_3_opr: Optional[str] = None,
        topic_0_2_opr: Optional[str] = None,
        topic_0_3_opr: Optional[str] = None,
        topic_1_3_opr: Optional[str] = None,
    ):
        """This is an alternative to the native eth_getLogs. An address and/or
        topic_x parameters are required. When multiple topic_x parameters are
        used, the topic_x_y_opr ("and"/"or" operator) is also required.

        **.. note:: Only the first 1000 results are returned.**

        :param from_block: Start block of the query
        :type from_block: int
        :param to_block: End block of the query
        :type to_block: int
        :param address: Address of the logs
        :type address: str
        :param topic_0: Topic 0 in the logs, defaults to None
        :type topic_0: Optional[str], optional
        :param topic_1: Topic 1 in the logs, defaults to None
        :type topic_1: Optional[str], optional
        :param topic_2: Topic 2 in the logs, defaults to None
        :type topic_2: Optional[str], optional
        :param topic_3: Topic 3 in the logs, defaults to None
        :type topic_3: Optional[str], optional
        :param topic_0_1_opr: Logical operator between topic 0 and 1,
                              defaults to None
        :type topic_0_1_opr: Optional[str], optional
        :param topic_1_2_opr: Logical operator between topic 1 and 2,
                              defaults to None
        :type topic_1_2_opr: Optional[str], optional
        :param topic_2_3_opr: Logical operator between topic 2 and 3,
                              defaults to None
        :type topic_2_3_opr: Optional[str], optional
        :param topic_0_2_opr: Logical operator between topic 0 and 2,
                              defaults to None
        :type topic_0_2_opr: Optional[str], optional
        :param topic_0_3_opr: Logical operator between topic 0 and 3,
                              defaults to None
        :type topic_0_3_opr: Optional[str], optional
        :param topic_1_3_opr: Logical operator between topic 1 and 3,
                              defaults to None
        :type topic_1_3_opr: Optional[str], optional
        :return: _description_
        :rtype: _type_
        """
        return "".join(
            filter(
                None,
                (
                    fields.MODULE,
                    modules.LOGS,
                    fields.ACTION,
                    actions.GET_LOGS,
                    fields.FROM_BLOCK,
                    str(from_block),
                    fields.TO_BLOCK,
                    str(to_block),
                    fields.ADDRESS,
                    address,
                    # topic 0
                    fields.TOPIC_0,
                    topic_0,
                    #
                    # Everything below is optional. If not provided by user, then
                    # they remain empty and do not affect the tail of the url.
                    #
                    # topic 0_x operators
                    fields.TOPIC_0_1_OPR * bool(topic_0_1_opr),
                    topic_0_1_opr,
                    fields.TOPIC_0_2_OPR * bool(topic_0_2_opr),
                    topic_0_2_opr,
                    fields.TOPIC_0_3_OPR * bool(topic_0_3_opr),
                    topic_0_3_opr,
                    # topic 1
                    fields.TOPIC_1 * bool(topic_1),
                    topic_1,
                    # topic 1_x operato,
                    fields.TOPIC_1_2_OPR * bool(topic_1_2_opr),
                    topic_1_2_opr,
                    fields.TOPIC_1_3_OPR * bool(topic_1_3_opr),
                    topic_1_3_opr,
                    # topic 2
                    fields.TOPIC_2 * bool(topic_2),
                    topic_2,
                    # topic 2_x operators
                    fields.TOPIC_2_3_OPR * bool(topic_2_3_opr),
                    topic_2_3_opr,
                    # topic 3
                    fields.TOPIC_3 * bool(topic_3),
                    topic_3,
                ),
            )
        )


class ProLogs(Logs):
    pass
    """
    Placeholder as there is currrently no endpoint for this class.

    """
