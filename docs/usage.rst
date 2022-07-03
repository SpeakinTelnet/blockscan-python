=====
Usage
=====

.. note:: The endpoints are not filtered on a per-chain basis. 
    Refer to blockscan docs in case your call fails.

Prerequisite
************
- This package to be installed (``pip install blockscan-python``)
- The chain ID you want to connect to.
        Refer to `chainlist <https://chainlist.org/>`_ if unknown
- Specific chain API Token provided by `blockscan <https://blockscan.com>`_
       (i.e: An `etherscan.io <https://etherscan.io>`_ token for Ethereum)

       Exception: Any Blockscout chain takes an empty string "", No token required

Create a connection client
**************************

The connection can be created as *Sync*:

.. code-block:: python

        >>> from blockscan import Blockscan
        
        # Sync connection to etherscan.io
        >>> client = blockscan(1, "MYAPITOKEN", is_async=False)
        >>> client.accounts.get_currency_balance(
                "0x0000000000000000000000000000000000000000"
                )
        '11400022397988649428803'

But will default to *Async* if no parameter is provided:

.. code-block:: python

        >>> from blockscan import BlockScan
        
        #Async connection to bscscan.com
        >>> client = Blockscan(56, "MYAPITOKEN")
        >>> bal = await client.accounts.get_currency_balance(
                        "0x0000000000000000000000000000000000000000"
                        )
        >>> print(bal)
        '1073557893975925234717'

See below for the full list of parameters available:

.. autoclass:: blockscan.Blockscan
