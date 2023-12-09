import pytest
import requests
from utils.utils import url_with_user_id


@pytest.mark.timeout(10)
def test_delete_user_by_id(valid_user, users_base_url, add_headers) -> None:
    ''' sanity of delete user by id '''
    user_id = valid_user['id']
    response = requests.delete(url_with_user_id(users_base_url, user_id), headers=add_headers)
    assert response.status_code == 200, response.text


@pytest.mark.timeout(10)
def test_delete_user_that_not_exist_in_db(invalid_user, users_base_url, add_headers) -> None:
    ''' verify we cant delete user that not exist in db (maybe i could do it hard coded instead of random id)'''
    user_id = invalid_user
    response = requests.delete(url_with_user_id(users_base_url, user_id), headers=add_headers)
    assert response.status_code == 404
    assert response.json()['message'] == f"User not found"
