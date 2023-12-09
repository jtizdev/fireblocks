import requests
import pytest
from tests.helpers import filter_by


@pytest.mark.timeout(10)
@pytest.mark.parametrize("filter_value, filter_name", [
    ("omri", "name")])
def test_get_user_filter_by_name(valid_user, users_base_url, add_headers, filter_value, filter_name) -> None:
    ''' sanity of filter user by name'''
    response = requests.get(users_base_url, params=filter_by(filter_value, filter_name), headers=add_headers)

    assert response.status_code == 200, response.text
    assert response.json()[0]['name'] == filter_value, response.text


@pytest.mark.timeout(10)
@pytest.mark.parametrize("filter_value, filter_name", [
    (0, "balance")])
def test_get_user_filter_by_balance(valid_user, users_base_url, add_headers, filter_value, filter_name) -> None:
    ''' sanity of filter user by balance'''
    response = requests.get(users_base_url, params=filter_by(filter_value, filter_name), headers=add_headers)

    assert response.status_code == 200, response.text
    assert response.json()[0]['balance'] == filter_value, response.text


@pytest.mark.timeout(10)
@pytest.mark.parametrize("filter_value, filter_name", [
    ("ahmed", "name")])
def test_get_users_by_name_not_exist_in_db(invalid_user, users_base_url, add_headers, filter_value,
                                           filter_name) -> None:
    ''' verify we can get user by name that not exist in db, we get empty list'''
    response = requests.get(users_base_url, params=filter_by(filter_value, filter_name), headers=add_headers)

    assert response.status_code == 200, response.text
    assert response.json() == [], response.text


@pytest.mark.timeout(10)
@pytest.mark.parametrize("filter_value, filter_name", [
    ("jose'", "name")])
def test_get_users_with_unique_chars_in_name(users_base_url, add_headers, filter_value, filter_name) -> None:
    ''' verify we can get user with unique chars in name'''
    response = requests.get(users_base_url, params=filter_by(filter_value, filter_name), headers=add_headers)

    assert response.status_code == 200, response.text
    assert response.json()[0]['name'] == filter_value, response.text


@pytest.mark.timeout(10)
@pytest.mark.parametrize("filter_value, filter_name", [
    ("omriiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii", "name")])
def get_user_with_long_name(users_base_url, add_headers, filter_value, filter_name) -> None:
    ''' verify we can get user with long name'''
    response = requests.get(users_base_url, params=filter_by(filter_value, filter_name), headers=add_headers)

    assert response.status_code == 200, response.text
    assert response.json()[0]['name'] == filter_value, response.text


@pytest.mark.timeout(10)
@pytest.mark.parametrize("filter_value, filter_name", [
    ("king omri", "name")])
def test_get_users_with_name_contain_space(users_base_url, add_headers, filter_value, filter_name) -> None:
    ''' verify we can get user with name contain space'''
    response = requests.get(users_base_url, params=filter_by(filter_value, filter_name), headers=add_headers)

    assert response.status_code == 200, response.text
    assert response.json()[0]['name'] == filter_value, response.text


@pytest.mark.timeout(10)
@pytest.mark.parametrize("filter_value, filter_name", [
    (" ", "name")])
def test_get_users_with_empty_string_name(users_base_url, add_headers, filter_value, filter_name) -> None:
    ''' verify we can get user with empty string name'''
    response = requests.get(users_base_url, params=filter_by(filter_value, filter_name), headers=add_headers)

    assert response.status_code == 200, response.text
    assert response.json()[0]['name'] == filter_value, response.text


@pytest.mark.timeout(10)
@pytest.mark.parametrize("filter_value, filter_name", [
    ("name", "name")])
def test_get_users_with_the_name_name(users_base_url, add_headers, filter_value, filter_name) -> None:
    ''' verify we can get user with the name name'''
    response = requests.get(users_base_url, params=filter_by(filter_value, filter_name), headers=add_headers)

    assert response.status_code == 200, response.text
    assert response.json()[0]['name'] == filter_value, response.text


@pytest.mark.timeout(10)
def test_get_users_by_id(users_base_url, add_headers, valid_user) -> None:
    """ this test is get user by id and compare the id with the id in the response"""
    user_id = valid_user['id']
    response = requests.get(users_base_url, params=filter_by(user_id, "id"), headers=add_headers)

    assert response.status_code == 200, response.text
    assert response.json()[0]['id'] == user_id, response.text
