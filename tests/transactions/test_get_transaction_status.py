import requests
import pytest
from utils.utils import url_with_transaction_id


@pytest.mark.timeout(10)
def test_get_transaction_status_by_id(valid_transaction, transactions_status_url, add_headers) -> None:
    ''' sanity of get transaction status by id'''
    transaction_id = valid_transaction.text
    response = requests.get(url_with_transaction_id(transactions_status_url, transaction_id), headers=add_headers)
    assert response.status_code == 200
    assert response.text is not None


@pytest.mark.timeout(10)
def test_get_transaction_that_not_exist_in_db(invalid_transaction, transactions_status_url, add_headers) -> None:
    ''' verify we cant get transaction status that not exist in db'''
    transaction_id = invalid_transaction
    response = requests.get(url_with_transaction_id(transactions_status_url, transaction_id), headers=add_headers)
    assert response.status_code == 404
    assert response.json()['message'] == f"Could not find transaction with id: {transaction_id}"
