================
blockscan-python
================

This package was created in the hope to provide a multi-chain API 
wrapper for the blockscan.com endpoints and reduce the overhead of
using multiple single chain wrapper.

.. note::
        The following blockchains from `blockscout.com <https://blockscout.com>`_ are also
        provided *BUT* it's because blockscout offers the API for ``developers transitioning
        their applications from Etherscan to BlockScout``. If they deprecate those API in the 
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

Donate 
------

I made this has a fun side project and it's free for anyone to use.
If you like it and wish to donate here's a few of my crypto wallets. 

.. _tbl-grid:

+----------------------------------------+--------------------------------------+-----------------------------------------+
| Ethereum and L2s (0x29006...)          | Monero (85tBS7YSrM5...)              | Peercoin (PBzj1ZwMDW...)                |
|                                        |                                      |                                         |
+========================================+======================================+=========================================+
| .. figure:: _qrcodes/ethereum.png      | .. figure:: _qrcodes/monero.png      | .. figure:: _qrcodes/peercoin.png       |
+----------------------------------------+--------------------------------------+-----------------------------------------+


* Free software: MIT license
* Documentation: https://blockscan-python.readthedocs.io.

Credits
-------

Credits to `@pcko1 <https://github.com/pcko1>`_ for making the 
bscscan-python that was used as the base for this package



Table of Contents
-----------------

.. toctree::
   :maxdepth: 1
   :caption: Overview

   usage
   contributing
   history

.. toctree::
   :maxdepth: 1
   :caption: API

   accounts
   blocks
   contracts
   gas_tracker
   logs
   proxy
   stats
   tokens
   transactions

Indices and tables
------------------
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
