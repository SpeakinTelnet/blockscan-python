from blockscan.enums.actions_enum import ActionsEnum as actions
from blockscan.enums.fields_enum import FieldsEnum as fields
from blockscan.enums.modules_enum import ModulesEnum as modules
from blockscan.modules.module import Module


class Contracts(Module):
    """ """

    @staticmethod
    def get_contract_abi(contract_address: str):
        """Get ABI for a specific contract, if uploaded.

        :param contract_address: Target contract address.
        :type contract_address: str

        :returns: ABI as a string.
        :rtype: str

        """
        return (
            f"{fields.MODULE}"
            f"{modules.CONTRACT}"
            f"{fields.ACTION}"
            f"{actions.GET_ABI}"
            f"{fields.ADDRESS}"
            f"{contract_address}"
        )

    @staticmethod
    def get_contract_source_code(contract_address: str):
        """Get source code for a specific contract, if uploaded.

        :param contract_address: Target contract address.
        :type contract_address: str

        :returns: Source code in a list of dictionaries of various data.
        :rtype: List[dict]

        """
        return (
            f"{fields.MODULE}"
            f"{modules.CONTRACT}"
            f"{fields.ACTION}"
            f"{actions.GET_SOURCE_CODE}"
            f"{fields.ADDRESS}"
            f"{contract_address}"
        )


class ProContracts(Contracts):
    pass
    """
    Placeholder as there is currrently no endpoint for this class

    """
