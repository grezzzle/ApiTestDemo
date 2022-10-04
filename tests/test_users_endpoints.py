import helpers.api as api
import pytest

# Base URL
BASE_URL = "https://reqres.in"

# Get and validate user info from - /api/user/2
@pytest.mark.order1
def test_user_info():
    user_info = api.ReqresApiTesting(BASE_URL)
    response = user_info.api_user_info()
    assert response.status == 200
    assert response.response.get('data').get('name') == 'fuchsia rose'
    assert response.response.get('data').get('id')


# Get and validate users list info from - api/users?page=1
@pytest.mark.order2
def test_users_list():
    user_info = api.ReqresApiTesting(BASE_URL)
    response = user_info.api_users_list()
    assert response.status == 200
    assert response.response.get('total') == 12
    assert response.response.get('data')[0].get('id')


# Test login with demo user data
@pytest.mark.order3
def test_login():
    user_info = api.ReqresApiTesting(BASE_URL)
    response = user_info.api_login()
    assert response.status == 200
    assert response.response.get('token')
