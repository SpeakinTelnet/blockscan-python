import pytest
import json
from blockscan import Blockscan


@pytest.fixture(scope="session")
def client():
    with Blockscan(1000000000000, "TEST", is_async=False, debug=True, pro=True) as bs:
        yield bs


@pytest.fixture(scope="session")
def tester_client():
    with Blockscan(1000000000000, "TEST", is_async=False, testing=True) as bs:
        yield bs


@pytest.fixture(scope="function")
async def async_client():
    async with Blockscan(1000000000000, "TEST", debug=True, pro=True) as bs:
        yield bs


@pytest.fixture
def accounts():
    with open("tests/modules/accounts.json", "r") as f:
        return json.load(f)


@pytest.fixture
def gas_tracker():
    with open("tests/modules/gas_tracker.json", "r") as f:
        return json.load(f)


@pytest.fixture
def blocks():
    with open("tests/modules/blocks.json", "r") as f:
        return json.load(f)


@pytest.fixture
def contracts():
    with open("tests/modules/contracts.json", "r") as f:
        return json.load(f)


@pytest.fixture
def logs():
    with open("tests/modules/logs.json", "r") as f:
        return json.load(f)


@pytest.fixture
def proxy():
    with open("tests/modules/proxy.json", "r") as f:
        return json.load(f)


@pytest.fixture
def stats():
    with open("tests/modules/stats.json", "r") as f:
        return json.load(f)


@pytest.fixture
def tokens():
    with open("tests/modules/tokens.json", "r") as f:
        return json.load(f)


@pytest.fixture
def transactions():
    with open("tests/modules/transactions.json", "r") as f:
        return json.load(f)
