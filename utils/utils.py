import os


def get_url(suffix: str):
    ''' get base url to send and add suffix'''
    return os.environ.get("BASE_URL") + suffix


def get_token():
    ''' get token to access the api'''
    return os.environ.get("TOKEN")


def create_headers() -> dict[str, str]:
    ''' create headers with token
    Returns:
        dict: headers with token
        '''
    return {"Authorization": f"Bearer {get_token()}"}


def url_with_user_id(users_base_url: str, id='2106'):
    return f"{users_base_url}/{id}"


def url_with_transaction_id(transactions_base_url: str, id: str = 'f391d611-989b-4c8f-bbcf-f68459a8aaeb'):
    '''create url with transaction id
    Args:
        transactions_base_url(str): base url for transactions
        id(str): transaction id
        Returns:
        str: url with transaction id
            '''
    return f"{transactions_base_url}/{id}"
