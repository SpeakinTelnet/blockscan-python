================
blockscan-python
================

This package was created in the hope to provide a multi-chain API 
wrapper for the blockscan.com endpoints and reduce the overhead of
using multiple single chain wrapper.

Note
----

The following blockchains from `blockscout.com <https://blockscout.com>`_ are also
provided *BUT* it's because blockscout offers the API for `developers transitioning
their applications from Etherscan to BlockScout <https://blockscout.com/etc/mainnet/api-docs>`_. If they deprecate those API in the 
future so will this package.

- Gnosis (100)
- Ethereum Classic (61)
- Ethereum Classic Mordor (63)
- Ethereum Classic Kotti (6)
- POA Core (99)
- POA Sokol (77)
- Artis Sigma1 (246529)
- RSK (30)
- Hoo Smart Chain (70) (This one is technicaly part of blockscan.com but is built on top of blockscout)




Installation
------------

Blockscan-python can be installed using ``pip`` as follows:

.. code-block:: console

   $ pip install blockscan-python

Usage
-----

Refer to the `full documentation <https://blockscan-python.readthedocs.io>`_
for the list of endpoints and the specific blockscan provider for compatibility.
This package doesn't filter the endpoints on a per-chain basis.
This means that some calls will fails if the provider doesn't support it.


Prerequisite
************

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

The full list of parameters is available in the `documentation <https://blockscan-python.readthedocs.io/usage.html#create-a-connection>`_



Donate 
------

I made this has a fun side project and it's free for anyone to use.
If you like it and wish to donate here's a few of my crypto wallets. 

.. _tbl-grid:

+----------------------------------------+--------------------------------------+-----------------------------------------+
| Ethereum and L2s (0x29006...)          | Monero (85tBS7YSrM5...)              | Peercoin (PBzj1ZwMDW...)                |
|                                        |                                      |                                         |
+========================================+======================================+=========================================+
| |EthereumQR|                           | |MoneroQR|                           | |PeercoinQR|                            |
+----------------------------------------+--------------------------------------+-----------------------------------------+

.. |EthereumQR| image:: https://raw.githubusercontent.com/SpeakinTelnet/blockscan-python/master/docs/_qrcodes/ethereum.png
  :width: 300
  :alt: EthereumQR

.. |MoneroQR| image:: https://raw.githubusercontent.com/SpeakinTelnet/blockscan-python/master/docs/_qrcodes/monero.png
  :width: 300
  :alt: MoneroQR

.. |PeercoinQR| image:: https://raw.githubusercontent.com/SpeakinTelnet/blockscan-python/master/docs/_qrcodes/peercoin.png
  :width: 300
  :alt: PeerCoinQR

* Free software: MIT license
* Documentation: https://blockscan-python.readthedocs.io.

Credits
-------

Credits to `@pcko1 <https://github.com/pcko1>`_ for making the 
bscscan-python that was used as the base for this package

TO-DOs
------

- Add a reference table of the available Chain ID to the docs
