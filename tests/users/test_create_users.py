import pytest
import requests

'''
this class is for testing the create user endpoint yes, you can create a json object and send it to the endpoint 
without declaring in each test, i think its more explicit and more readable

'''


class TestCreateUser:
    @pytest.fixture(scope='function')
    def setup(self, users_base_url, add_headers, name, balance):
        self.users_base_url = users_base_url
        self.add_headers = add_headers
        self.name = name
        self.balance = balance

    @pytest.mark.timeout(10)
    @pytest.mark.parametrize('name, balance', [
        ("omri", 0),
        ("omri", 1)
    ])
    def test_create_user(self, setup, name, balance) -> None:
        ''' sanity of create user '''
        response = requests.post(self.users_base_url, headers=self.add_headers,
                                 json={"name": self.name, "balance": self.balance})
        assert response.status_code == 201, response.text

    @pytest.mark.timeout(10)
    @pytest.mark.parametrize('name, balance', [
        ("omri", 0), ])
    def test_create_user_name_missing(self, setup, balance) -> None:
        ''' create user without name '''
        response = requests.post(self.users_base_url, headers=self.add_headers, json={"balance": self.balance})
        assert response.status_code == 500, response.text

    @pytest.mark.timeout(10)
    @pytest.mark.parametrize('name, balance', [
        ("omri", 0), ])
    def test_create_user_balance_missing(self, setup, name) -> None:
        ''' create user without balance '''
        response = requests.post(self.users_base_url, headers=self.add_headers, json={"name": self.name})
        assert response.status_code == 500, response.text

    @pytest.mark.timeout(10)
    @pytest.mark.parametrize('name, balance', [
        ("omri", -1), ])
    def test_create_user_with_negative_balance(self, setup, name, balance) -> None:
        ''' verify we cant create user with negative balance'''
        response = requests.post(self.users_base_url, headers=self.add_headers, json={"name": self.name, "balance": -1})
        assert response.status_code == 400, response.text

    @pytest.mark.timeout(10)
    @pytest.mark.parametrize('name, balance', [
        ("omri", "0"), ])
    def test_create_user_when_balance_is_string(self, setup, name, balance) -> None:
        ''' verify we can create user when balance is string'''
        response = requests.post(self.users_base_url, headers=self.add_headers,
                                 json={"name": self.name, "balance": self.balance})
        assert response.status_code == 201, response.text

    @pytest.mark.timeout(10)
    @pytest.mark.parametrize('name, balance', [
        ("omri", 0), ])
    def test_create_user_with_optional_field(self, setup, name, balance) -> None:
        ''' verify we cant create user with optional field'''
        response = requests.post(self.users_base_url, headers=self.add_headers,
                                 data={"name": self.name, "balance": self.name, "optional_field": "optional"})
        assert response.status_code == 500, response.text

    @pytest.mark.timeout(10)
    @pytest.mark.parametrize('name, balance', [
        ("omri", 0), ])
    def test_create_user_with_balance_twice(self, setup, name, balance) -> None:
        ''' verify we can create user with balance twice, the first balance will be override'''
        response = requests.post(self.users_base_url, headers=self.add_headers,
                                 json={"name": self.name, "balance": self.balance, "balance": 1})
        assert response.status_code == 201, response.text

    @pytest.mark.timeout(10)
    @pytest.mark.parametrize('name, balance', [
        ("omri", 0.1), ])
    def test_create_user_with_decimal_balance(self, setup) -> None:
        response = requests.post(self.users_base_url, headers=self.add_headers,
                                 json={"name": self.name, "balance": self.balance})
        assert response.status_code == 500, response.text

    @pytest.mark.timeout(10)
    @pytest.mark.parametrize('name, balance', [
        ("omri", 10000000000000000), ])
    def test_create_user_with_large_balance(self, setup) -> None:
        ''' verify we cant create user with large balance'''
        response = requests.post(self.users_base_url, headers=self.add_headers,
                                 json={"name": self.name, "balance": self.balance})
        assert response.status_code == 500, response.text

    @pytest.mark.timeout(10)
    @pytest.mark.parametrize('name, balance', [
        ("", 0), ])
    def test_create_user_with_empty_string_name(self, setup, name, balance) -> None:
        ''' verify we can create user with empty string name'''
        response = requests.post(self.users_base_url, headers=self.add_headers,
                                 json={"name": self.name, "balance": self.balance})
        assert response.status_code == 201, response.text
