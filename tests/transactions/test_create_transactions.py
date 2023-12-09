import pytest
import requests


class TestCreateTransactions:
    @pytest.fixture(scope='function')
    def setup(self, transactions_create_url, add_headers, source_id, destination_id, amount):
        self.transactions_url = transactions_create_url
        self.add_headers = add_headers
        self.source_id = source_id
        self.destination_id = destination_id
        self.amount = amount

    @pytest.mark.timeout(10)
    @pytest.mark.parametrize('source_id, destination_id, amount', [
        (1, 2, 1),
        (2, 1, 1)
    ])
    def test_create_transaction(self, setup, source_id, destination_id, amount) -> None:
        ''' sanity of create transaction '''
        response = requests.post(self.transactions_url, headers=self.add_headers,
                                 json=self.transactions_body())
        assert response.status_code == 201, response.text

    @pytest.mark.timeout(10)
    @pytest.mark.parametrize('source_id, destination_id, amount', [
        (None, 2, 1),
        (None, 1, 1)
    ])
    def test_create_transactions_without_source_id(self, setup, source_id, destination_id, amount) -> None:
        ''' verify we cant create transaction without source id'''
        response = requests.post(self.transactions_url, headers=self.add_headers,
                                 json=self.transactions_body())
        assert response.status_code == 500, response.text

    @pytest.mark.timeout(10)
    @pytest.mark.parametrize('source_id, destination_id, amount', [
        (1, None, 1),
        (2, None, 1)
    ])
    def test_create_transactions_without_destination_id(self, setup, source_id, destination_id, amount) -> None:
        response = requests.post(self.transactions_url, headers=self.add_headers,
                                 json=self.transactions_body())
        assert response.status_code == 500, response.text

    @pytest.mark.timeout(10)
    @pytest.mark.parametrize('source_id, destination_id, amount', [
        (1, 2, None),
        (2, 1, None)
    ])
    def test_create_transactions_without_amount(self, setup, source_id, destination_id, amount) -> None:
        response = requests.post(self.transactions_url, headers=self.add_headers,
                                 json=self.transactions_body())
        assert response.status_code == 500, response.text

    @pytest.mark.timeout(10)
    @pytest.mark.parametrize('source_id, destination_id, amount', [
        (1, 2, -5),
        (2, 1, -10)
    ])
    def test_create_transaction_with_negative_amount(self, setup, source_id, destination_id, amount) -> None:
        ''' verify we can create transaction with negative amount'''
        response = requests.post(self.transactions_url, headers=self.add_headers,
                                 json=self.transactions_body())
        assert response.status_code == 201, response.text

    @pytest.mark.timeout(10)
    @pytest.mark.parametrize('source_id, destination_id, amount', [
        (1, 2, 0),
        (2, 1, 0)
    ])
    def test_create_transaction_with_zero_amount(self, setup, source_id, destination_id, amount) -> None:
        ''' verify we can create transaction with zero amount'''
        response = requests.post(self.transactions_url, headers=self.add_headers,
                                 json=self.transactions_body())
        assert response.status_code == 201, response.text

    @pytest.mark.timeout(10)
    @pytest.mark.parametrize('source_id, destination_id, amount', [
        (1, 2, 0.1),
        (2, 1, 0.1)
    ])
    def test_create_transaction_with_decimal_amount(self, setup, source_id, destination_id, amount) -> None:
        ''' verify we cant create transaction with decimal amount'''
        response = requests.post(self.transactions_url, headers=self.add_headers,
                                 json=self.transactions_body())
        assert response.status_code == 500, response.text

    @pytest.mark.timeout(10)
    @pytest.mark.parametrize('source_id, destination_id, amount', [
        (1, 1, 0),
        (2, 2, 0)
    ])
    def test_create_transaction_when_source_id_identical_to_destination_id(self, setup, source_id, destination_id,
                                                                           amount) -> None:
        ''' verify we can create transaction when source id identical to destination id'''
        response = requests.post(self.transactions_url, headers=self.add_headers,
                                 json=self.transactions_body())
        assert response.status_code == 201, response.text

    def transactions_body(self) -> dict:
        return {"sourceId": self.source_id, "destinationId": self.destination_id,
                "amount": self.amount}

