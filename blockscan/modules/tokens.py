from blockscan.enums.actions_enum import ActionsEnum as actions
from blockscan.enums.fields_enum import FieldsEnum as fields
from blockscan.enums.modules_enum import ModulesEnum as modules
from blockscan.enums.tags_enum import TagsEnum as tags
from blockscan.modules.module import Module


class Tokens(Module):
    """ """

    @staticmethod
    def get_total_supply_by_contract_address(contract_address: str):
        """Get total supply of token by its contract address.

        :param contract_address: Target contract address.
        :type contract_address: str

        :returns: Total supply of token behind target contract.
        :rtype: str

        """
        return (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.TOKEN_SUPPLY}"
            f"{fields.CONTRACT_ADDRESS}"
            f"{contract_address}"
        )

    @staticmethod
    def get_circulating_supply_by_contract_address(contract_address: str):
        """Get circulating supply of token by its contract address.

        :param contract_address: Target contract address.
        :type contract_address: str

        :returns: Circulating supply of token behind target contract.
        :rtype: str

        """
        return (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.TOKEN_CSUPPLY}"
            f"{fields.CONTRACT_ADDRESS}"
            f"{contract_address}"
        )

    @staticmethod
    def get_acc_balance_by_token_contract_address(contract_address: str, address: str):
        """Get account balance given a contract address.

        :param contract_address: Target contract address.
        :type contract_address: str
        :param address: Target wallet address.
        :type address: str

        :returns: The target token balance of target account.
        :rtype: str

        """
        return (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TOKEN_BALANCE}"
            f"{fields.CONTRACT_ADDRESS}"
            f"{contract_address}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.TAG}"
            f"{tags.LATEST}"
        )


class ProTokens(Tokens):
    @staticmethod
    def get_hist_token_supply_by_contract_address_by_block_no(
        contract_address: str, block_no: int
    ) -> str:
        return (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.TOKEN_SUPPLY_HISTORY}"
            f"{fields.CONTRACT_ADDRESS}"
            f"{contract_address}"
            f"{fields.BLOCKNO}"
            f"{block_no}"
        )

    @staticmethod
    def get_hist_token_account_balance_for_token_contract_address_by_block_no(
        contract_address: str, address: str, block_no: int
    ) -> str:
        return (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TOKEN_BALANCE_HISTORY}"
            f"{fields.CONTRACT_ADDRESS}"
            f"{contract_address}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.BLOCKNO}"
            f"{block_no}"
        )

    @staticmethod
    def get_token_info_by_contract_address(contract_address: str) -> str:
        return (
            f"{fields.MODULE}"
            f"{modules.TOKEN}"
            f"{fields.ACTION}"
            f"{actions.TOKEN_INFO}"
            f"{fields.CONTRACT_ADDRESS}"
            f"{contract_address}"
        )
