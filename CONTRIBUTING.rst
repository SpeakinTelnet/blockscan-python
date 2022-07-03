.. highlight:: shell

============
Contributing
============

Contributions are welcome, either in the form of reports or fixes. Refer to the 
`GitHub repo <https://github.com/SpeakinTelnet/blockscan-python>`_ for issues and
pull requests.

Report Bugs
-----------

If you are reporting a bug, please include:

* Your operating system.
* If the issue is blockchain specific.
* Detailed steps to reproduce the bug.

Enhancement Guidelines
----------------------

Adding a new endpoint
~~~~~~~~~~~~~~~~~~~~~

As the unittest are mocked I decided to derive the mocking from an actual call
instead of blank responses. This is because the unittest will check that the 
function works but not if the endpoint call does.

So, as a best practice, if you're adding an endpoint please run it first in that
format:

.. code-block:: python

    from blockscan import Blockscan

    >>> client = Blockscan(1, "ACTUALAPITOKEN", is_async=False, testing=True)
    >>> mock_data = bs.accounts.get_currency_balance(
                        #Important to use keyword arguments here
                        address="0x0000000000000000000000000000000000000000"
                        )
    >>> print(mock_data)

    {
    "get_currency_balance": {
        "url": "https://api.test.io/api?module=account&action=balance&address=0x0000000000000000000000000000000000000000&tag=latest&apikey=TEST",
        "kwargs": {},
        "response": {
            "status": "1",
            "message": "OK",
            "result": "11400029508376005006696"
        },
        "assertion": "11400029508376005006696"
      }
    }

Then just append the appropriate .json file in the tests/modules/ folder with
your result. This alone will make sure pytest runs the new enpoint.

Adding a new blockchain
~~~~~~~~~~~~~~~~~~~~~~~

This is a simple as appending the blockscan/blockchains.py files with your
blockchain info in the following format:

.. code-block:: json

    1: {
        "url": "https://api.etherscan.io/api?",
        "price": "ethprice",
        "supply": "ethsupply",
        "daily_price": "ethdailyprice",
        "daily_market_cap": "ethdailymarketcap",
      }
    
`1` is the blockchain ID

``price``, ``supply``, ``daily_price``, and ``daily_market_cap`` are all taken from the ``stats`` 
module and have to be explicit as they can vary per blockchain. Refer to the 
`blockscan.com <https://blockscan.com>`_ specific provider for details.
If the endpoint doesn't exist, use the default ethereum value 

Pull Request Guidelines
-----------------------

Your pull request should pass the *nox* test. 

nox will run ``black``, ``flake8``, ``pytest``, and regenerate the docs

Deploying
---------

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.rst).
Then run::

$ bump2version patch # possible: major / minor / patch
$ git push
$ git push --tags

Travis will then deploy to PyPI if tests pass.
