import pytest
from utils.utils import get_url, create_headers
from tests.helpers import generate_user, generate_fake_user_id


@pytest.fixture(scope='module')
def users_base_url():
    return get_url("/users")


@pytest.fixture(scope='module')
def add_headers():
    return create_headers()


@pytest.fixture
def valid_user(users_base_url, add_headers):
    return generate_user(users_base_url, add_headers)


@pytest.fixture
def invalid_user(users_base_url, add_headers):
    return generate_fake_user_id()


