import pytest
import requests
from utils.utils import url_with_user_id


class TestUpdateUsersTests:

    @pytest.fixture(scope='function')
    def setup(self, users_base_url, add_headers):
        self.users_base_url = users_base_url
        self.add_headers = add_headers
        self.name = "omri"
        self.balance = 0

    @pytest.mark.timeout(10)
    @pytest.mark.parametrize('name, balance', [
        ("omri", 0), ])
    def test_update_user_by_id(self, setup, name, balance) -> None:
        ''' sanity of update user by id'''
        response = requests.patch(url_with_user_id(self.users_base_url), headers=self.add_headers,
                                  json={"name": self.name, "balance": self.balance})
        assert response.status_code == 200, response.text

    @pytest.mark.timeout(10)
    @pytest.mark.parametrize('name, balance', [
        ("omri", 0), ])
    def test_update_user_that_not_exist_in_db(self, setup, name, balance) -> None:
        ''' verify we cant update user that not exist in db'''
        response = requests.patch(url_with_user_id(self.users_base_url, '0001'),
                                  headers=self.add_headers,
                                  json={"name": self.name, "balance": self.balance})
        assert response.status_code == 400, response.text

    @pytest.mark.timeout(10)
    @pytest.mark.parametrize('name, balance', [
        ("", 0), ])
    def test_update_user_with_empty_string_name(self, setup, name, balance) -> None:
        ''' verify we can update user with empty string name'''
        response = requests.patch(url_with_user_id(self.users_base_url), headers=self.add_headers,
                                  json={"name": self.name, "balance": self.balance})
        assert response.status_code == 200, response.text

    @pytest.mark.timeout(10)
    def test_update_user_with_decimal_balance(self, setup) -> None:
        ''' verify we cant update user with decimal balance'''
        response = requests.patch(url_with_user_id(self.users_base_url), headers=self.add_headers,
                                  json={"name": self.name, "balance": 0.1})
        assert response.status_code == 500, response.text

    @pytest.mark.timeout(10)
    @pytest.mark.parametrize('name, balance', [
        ("omri", 0), ])
    def test_update_user_with_optional_field(self, setup, name, balance) -> None:
        ''' verify we can update user with optional field'''
        response = requests.patch(url_with_user_id(self.users_base_url), headers=self.add_headers,
                                  json={"name": self.name, "balance": self.balance,
                                        "optional_field": "optional"})
        assert response.status_code == 200, response.text

    @pytest.mark.timeout(10)
    def test_update_user_with_negative_balance(self, setup) -> None:
        ''' verify we cant update user with negative balance'''
        response = requests.patch(url_with_user_id(self.users_base_url), headers=self.add_headers,
                                  json={"name": self.name, "balance": -1})
        assert response.status_code == 400, response.text

    @pytest.mark.timeout(10)
    @pytest.mark.parametrize('name, balance', [
        ("omri", "0"), ])
    def test_update_user_without_name(self, setup, name, balance) -> None:
        ''' verify we can update user without update name'''
        response = requests.patch(url_with_user_id(self.users_base_url), headers=self.add_headers,
                                  json={"balance": self.balance})
        assert response.status_code == 200, response.text

    @pytest.mark.timeout(10)
    @pytest.mark.parametrize('name, balance', [
        ("omri", 0), ])
    def test_update_user_without_balance(self, setup, name, balance) -> None:
        ''' verify we can update user name without update balance'''
        response = requests.patch(url_with_user_id(self.users_base_url), headers=self.add_headers,
                                  json={"name": self.name})
        assert response.status_code == 200, response.text
