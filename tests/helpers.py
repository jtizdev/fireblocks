import requests
import random
import uuid


def generate_user(users_base_url: str, add_headers: dict) -> dict:
    '''
    generate user with default values that can be override
    Args:
        users_base_url(str): url for create user
        add_headers(dict): headers for the request

    Returns:

    '''
    response = requests.post(users_base_url, headers=add_headers, json={"name": "omri", "balance": "0"})
    return response.json()


def generate_fake_user_id() -> int:
    '''
    generate fake user id
    Returns:
        int: fake user id

    '''
    return random.randint(0000, 9999)


def filter_by(filter_value: str, filter_name: str = 'name') -> str:
    '''
    generate filter to query the users
    Args:
        filter_value(str): value to filter on
        filter_name(str): name of the filter to query on

    Returns:

    '''
    # i can extract also the actions but for my tests now i dont need it, this will be on the backlog for now
    return f'filter={filter_name}||$eq||{filter_value}'


def generate_transaction(transactions_create_url: str, add_headers: dict, source_id=1, destination_id=1, amount=1):
    '''
    generate transaction with default values that can be override
    Args:
        transactions_create_url(str): url for create transaction
        add_headers (dict): headers for the request
        source_id (int): source id for the transaction
        destination_id (int): destination id for the transaction
        amount(int): amount for the transaction

    Returns:
        response: response from the request

    '''
    response = requests.post(transactions_create_url, headers=add_headers,
                             json={"sourceId": source_id, "destinationId": destination_id,
                                   "amount": amount})
    return response


def generate_fake_transaction_id() -> str:
    '''
    generate fake transaction id
    Returns:
        str: fake transaction id


    '''
    return str(uuid.uuid4())
