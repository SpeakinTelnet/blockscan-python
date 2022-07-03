from blockscan.enums.actions_enum import ActionsEnum as actions
from blockscan.enums.fields_enum import FieldsEnum as fields
from blockscan.enums.modules_enum import ModulesEnum as modules
from blockscan.modules.module import Module


class Transactions(Module):
    """ """

    @staticmethod
    def get_contract_execution_status(txhash: str) -> str:
        return (
            f"{fields.MODULE}"
            f"{modules.TRANSACTION}"
            f"{fields.ACTION}"
            f"{actions.GET_STATUS}"
            f"{fields.TXHASH}"
            f"{txhash}"
        )

    @staticmethod
    def get_tx_receipt_status(txhash: str):
        """Check the status of a transaction receipt.

        :param txhash: Target tx hash.
        :type txhash: str

        :returns: The status code.
        :rtype: str

        """
        return (
            f"{fields.MODULE}"
            f"{modules.TRANSACTION}"
            f"{fields.ACTION}"
            f"{actions.GET_TX_RECEIPT_STATUS}"
            f"{fields.TXHASH}"
            f"{txhash}"
        )


class ProTransactions(Transactions):
    pass
    """
    Placeholder as there is currrently no endpoint for this class.

    """
