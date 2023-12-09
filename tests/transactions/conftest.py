import pytest
from utils.utils import get_url, create_headers
from tests.helpers import generate_transaction, generate_fake_transaction_id


@pytest.fixture(scope='module')
def transactions_base_url():
    return get_url("/transactions")


@pytest.fixture(scope='module')
def transactions_create_url():
    return get_url("/transactions/create")


@pytest.fixture(scope='module')
def transactions_status_url():
    return get_url("/transactions/status")


@pytest.fixture(scope='module')
def add_headers():
    return create_headers()


@pytest.fixture(scope='module')
def valid_transaction(transactions_create_url, add_headers):
    return generate_transaction(transactions_create_url, add_headers)


@pytest.fixture(scope='module')
def invalid_transaction():
    return generate_fake_transaction_id()
