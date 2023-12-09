import requests
import pytest
from utils.utils import url_with_user_id


@pytest.mark.timeout(10)
def test_get_user_by_id(valid_user, users_base_url, add_headers) -> None:
    ''' sanity of get user by id '''
    user_id = valid_user['id']
    response = requests.get(url_with_user_id(users_base_url, user_id), headers=add_headers)
    assert response.status_code == 200
    assert response.json()['id'] == user_id


@pytest.mark.timeout(10)
def test_get_user_that_not_exist_in_db(invalid_user, users_base_url, add_headers) -> None:
    ''' verify we cant get user that not exist in db'''
    user_id = invalid_user
    response = requests.get(url_with_user_id(users_base_url, user_id), headers=add_headers)
    assert response.status_code == 404
    assert response.json()['message'] == "User not found"


@pytest.mark.timeout(10)
def test_get_user_0000(users_base_url, add_headers) -> None:
    ''' verify we cant get user with id 0000'''
    user_id = '0000'
    response = requests.get(url_with_user_id(users_base_url, user_id), headers=add_headers)
    assert response.status_code == 400
    assert response.json()['message'] == "Invalid param id. Number expected"


@pytest.mark.timeout(10)
def test_get_user_with_decimal_id(users_base_url, add_headers) -> None:
    ''' verify we cant get user with decimal id'''
    user_id = 0.1
    response = requests.get(url_with_user_id(users_base_url, user_id), headers=add_headers)
    assert response.status_code == 500


@pytest.mark.timeout(10)
def test_get_user_with_negative_id(users_base_url, add_headers) -> None:
    ''' verify we cant get user with negative id'''
    user_id = -1
    response = requests.get(url_with_user_id(users_base_url, user_id), headers=add_headers)
    assert response.status_code == 404
    assert response.json()['message'] == "User not found"
