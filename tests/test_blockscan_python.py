import pytest
import json
from aioresponses import aioresponses
import requests_mock
from blockscan.blockchains import blockchains
from blockscan import Blockscan


@requests_mock.Mocker(kw="mock")
def runner(func, data, *args, **kwargs):
    url = data["url"]
    get_response = data["response"]
    func_kwargs = data["kwargs"]
    assertion = data["assertion"]
    kwargs["mock"].get(url, json=get_response)
    func_response = func(**func_kwargs)
    assert assertion == func_response


@aioresponses()
async def async_runner(mocked, func, data, *args, **kwargs):
    url = data["url"]
    get_response = data["response"]
    func_kwargs = data["kwargs"]
    assertion = data["assertion"]
    mocked.get(url, body=json.dumps(get_response))
    func_response = await func(**func_kwargs)
    assert assertion == func_response


class TestSyncEndpoints:
    def test_sync_accounts(self, client, accounts, **kwargs):
        for func, data in accounts.items():
            obj = getattr(client.accounts, func)
            runner(func=obj, data=data)

    def test_sync_blocks(self, client, blocks, **kwargs):
        for func, data in blocks.items():
            obj = getattr(client.blocks, func)
            runner(func=obj, data=data)

    def test_sync_contracts(self, client, contracts, **kwargs):
        for func, data in contracts.items():
            obj = getattr(client.contracts, func)
            runner(func=obj, data=data)

    def test_sync_gas_tracker(self, client, gas_tracker, **kwargs):
        for func, data in gas_tracker.items():
            obj = getattr(client.gas_tracker, func)
            runner(func=obj, data=data)

    def test_sync_logs(self, client, logs, **kwargs):
        for func, data in logs.items():
            obj = getattr(client.logs, func)
            runner(func=obj, data=data)

    def test_sync_proxy(self, client, proxy, **kwargs):
        for func, data in proxy.items():
            obj = getattr(client.proxy, func)
            runner(func=obj, data=data)

    def test_sync_stats(self, client, stats, **kwargs):
        for func, data in stats.items():
            obj = getattr(client.stats, func)
            runner(func=obj, data=data)

    def test_sync_tokens(self, client, tokens, **kwargs):
        for func, data in tokens.items():
            obj = getattr(client.tokens, func)
            runner(func=obj, data=data)

    def test_sync_transactions(self, client, transactions, **kwargs):
        for func, data in transactions.items():
            obj = getattr(client.transactions, func)
            runner(func=obj, data=data)


class TestAsyncEndpoints:
    async def test_async_accounts(self, async_client, accounts, **kwargs):
        for func, data in accounts.items():
            obj = getattr(async_client.accounts, func)
            await async_runner(func=obj, data=data)

    async def test_async_blocks(self, async_client, blocks, **kwargs):
        for func, data in blocks.items():
            obj = getattr(async_client.blocks, func)
            await async_runner(func=obj, data=data)

    async def test_async_contracts(self, async_client, contracts, **kwargs):
        for func, data in contracts.items():
            obj = getattr(async_client.contracts, func)
            await async_runner(func=obj, data=data)

    async def test_async_gas_tracker(self, async_client, gas_tracker, **kwargs):
        for func, data in gas_tracker.items():
            obj = getattr(async_client.gas_tracker, func)
            await async_runner(func=obj, data=data)

    async def test_async_logs(self, async_client, logs, **kwargs):
        for func, data in logs.items():
            obj = getattr(async_client.logs, func)
            await async_runner(func=obj, data=data)

    async def test_async_proxy(self, async_client, proxy, **kwargs):
        for func, data in proxy.items():
            obj = getattr(async_client.proxy, func)
            await async_runner(func=obj, data=data)

    async def test_async_stats(self, async_client, stats, **kwargs):
        for func, data in stats.items():
            obj = getattr(async_client.stats, func)
            await async_runner(func=obj, data=data)

    async def test_async_tokens(self, async_client, tokens, **kwargs):
        for func, data in tokens.items():
            obj = getattr(async_client.tokens, func)
            await async_runner(func=obj, data=data)

    async def test_async_transactions(self, async_client, transactions, **kwargs):
        for func, data in transactions.items():
            obj = getattr(async_client.transactions, func)
            await async_runner(func=obj, data=data)


def test_blockchain_instanciation():
    for blockchain in blockchains:
        Blockscan(blockchain, "TEST", is_async=False)


def test_unknown_blockchain_string():
    with pytest.raises(Exception) as exc_info:
        Blockscan("badblockchain", "TEST", debug=True)
    assert exc_info.value.args[0] == "Chain ID badblockchain not recognized"


def test_unknown_blockchain_int():
    with pytest.raises(Exception) as exc_info:
        Blockscan(1000000000001321, "TEST", debug=True)
    assert exc_info.value.args[0] == "Chain ID 1000000000001321 not recognized"


def test_sync_accounts_as_tester(tester_client, accounts, **kwargs):
    for func, data in accounts.items():
        obj = getattr(tester_client.accounts, func)
        data["assertion"] = json.dumps({func: data}, indent=4)
        runner(func=obj, data=data)
