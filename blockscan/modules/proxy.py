from blockscan.enums.actions_enum import ActionsEnum as actions
from blockscan.enums.fields_enum import FieldsEnum as fields
from blockscan.enums.modules_enum import ModulesEnum as modules
from blockscan.enums.tags_enum import TagsEnum as tags
from blockscan.modules.module import Module


class Proxy(Module):
    """ """

    @staticmethod
    def get_proxy_block_number():
        """Get the number of the most recent block.

        :returns: The block number.
        :rtype: str

        """
        return (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_BLOCK_NUMBER}"
        )

    @staticmethod
    def get_proxy_block_by_number(tag: str):
        """Get information about a block by its block number.

        :param tag: The target block tag.
        :type tag: str

        :returns: Information about target block, including its transactions.
        :rtype: dict

        """
        return (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GET_BLOCK_BY_NUMBER}"
            f"{fields.TAG}"
            f"{tag}"
            f"{fields.BOOLEAN}"
            f"true"
        )

    @staticmethod
    def get_proxy_uncle_by_block_number_and_index(tag: str, index: str) -> str:
        """get information about a uncle by block number

        :param tag: The block number, in hex
        :type tag: str
        :param index: The position of the uncle's index in the block, in hex
        :type index: str

        :return: Information about target block
        :rtype: str
        """

        return (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GET_UNCLE_BY_BLOCK_NUMBER_AND_INDEX}"
            f"{fields.TAG}"
            f"{tag}"
            f"{fields.INDEX}"
            f"{index}"
        )

    @staticmethod
    def get_proxy_block_transaction_count_by_number(tag: str):
        """Get the number of transactions in a specific block.

        :param tag: The target block tag.
        :type tag: str

        :returns: The number of txs in the block using hex base format.
        :rtype: str

        """
        return (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GET_BLOCK_TRANSACTION_COUNT_BY_NUMBER}"
            f"{fields.TAG}"
            f"{tag}"
        )

    @staticmethod
    def get_proxy_transaction_by_hash(txhash: str):
        """Get tx information given its hash.

        :param txhash: Target transaction hash.
        :type txhash: str

        :returns: Standard tx data, including v,r,s values.
        :rtype: dict

        """
        return (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GET_TRANSACTION_BY_HASH}"
            f"{fields.TXHASH}"
            f"{txhash}"
        )

    @staticmethod
    def get_proxy_transaction_by_block_number_and_index(tag: str, index: str):
        """Get transaction by block number and tx index.

        :param tag: Target block tag.
        :type tag: str
        :param index: Target tx index.
        :type index: str

        :returns: Standard tx data, including v,r,s values.
        :rtype: dict

        """
        return (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GET_TRANSACTION_BY_BLOCK_NUMBER_AND_INDEX}"
            f"{fields.TAG}"
            f"{tag}"
            f"{fields.INDEX}"
            f"{index}"
        )

    @staticmethod
    def get_proxy_transaction_count(address: str):
        """Get number of transactions sent from an address.

        :param address: Target address.
        :type address: str

        :returns: Number of txs using hex base format.
        :rtype: str

        """
        return (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GET_TRANSACTION_COUNT}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.TAG}"
            f"{tags.LATEST}"
        )

    @staticmethod
    def get_proxy_transaction_receipt(txhash: str):
        """Get receipt of transaction from its hash.

        :param txhash: Target transaction hash.
        :type txhash: str

        :returns: Transaction receipt including logs.
        :rtype: dict

        """
        return (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GET_TRANSACTION_RECEIPT}"
            f"{fields.TXHASH}"
            f"{txhash}"
        )

    @staticmethod
    def get_proxy_call(to: str, data: str):
        """Executes a new message call immediately without
        creating a transaction on the block chain.

        :param to: Contract address to send message to.
        :type to: str
        :param data: Message data in bytecode.
        :type data: str

        :returns: The response to the message in hex base format.
        :rtype: str

        """
        return (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_CALL}"
            f"{fields.TO}"
            f"{to}"
            f"{fields.DATA}"
            f"{data}"
            f"{fields.TAG}"
            f"{tags.LATEST}"
        )

    @staticmethod
    def get_proxy_code_at(address: str):
        """Get contract bytecode at target address, if any.

        :param address: Address to query for bytecode.
        :type address: str

        :returns: The bytecode in hex base format.
        :rtype: str

        """
        return (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GET_CODE}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.TAG}"
            f"{tags.LATEST}"
        )

    @staticmethod
    def get_proxy_storage_position_at(position: str, address: str):
        """Get the value from a storage position at a given address.

        :param position: Target position in hex base format.
        :type position: str
        :param address: Target address.
        :type address: str

        :returns: Value in hex base format.
        :rtype: str

        """
        return (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GET_STORAGE_AT}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.POSITION}"
            f"{position}"
            f"{fields.TAG}"
            f"{tags.LATEST}"
        )

    @staticmethod
    def get_proxy_gas_price():
        """Get current gas price in wei.

        :returns: Gas price in wei and hex base format.
        :rtype: str
        """
        return (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GAS_PRICE}"
        )

    @staticmethod
    def get_proxy_est_gas(
        from_addr: str,
        to_addr: str,
        data: str,
        value: str,
        gas_price: str,
        gas: str,
    ):
        """Get gas estimate by making a dummy call/transaction that is not
        added to the blockchain and returns the hypothetically used gas.

        :param from_addr: Sender of transaction.
        :type from_addr: str
        :param to_addr: Receiver of transaction.
        :type to_addr: str
        :param data: Data of transaction.
        :type data: str
        :param value: Value of transaction.
        :type value: str
        :param gas_price: Gas price of transaction.
        :type gas_price: str
        :param gas: Gas of transaction.
        :type gas: str

        :returns: Estimated used gas for transaction.
        :rtype: str
        """
        return (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_ESTIMATE_GAS}"
            f"{fields.DATA}"
            f"{data}"
            f"{fields.FROM}"
            f"{from_addr}"
            f"{fields.TO}"
            f"{to_addr}"
            f"{fields.VALUE}"
            f"{value}"
            f"{fields.GAS_PRICE}"
            f"{gas_price}"
            f"{fields.GAS}"
            f"{gas}"
        )


class ProProxy(Proxy):
    pass
    """
    Placeholder as there is currrently no endpoint for this class.

    """
