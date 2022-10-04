from jsonschema import validate
import helpers.requests as requests
from schemas import schema_user_info, schema_users_list, schema_login

# Test user Login\Password
login_dict = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

# API endpoints
GET_USER_INFO = "/api/user/2"
GET_USERS_LIST = "/api/users?page=1"
POST_LOGIN = "/api/login"


class ReqresApiTesting:

    def __init__(self, base_url):
        """
            Init object
            :param Base URL, default - https://reqres.in
        """
        self.base_url = base_url

    def api_user_info(self):
        """
            :return: Custom ResponseModel object with status and json with info about user.
                For more information about ResponseModel obj check helpers.requests.
        """
        response = requests.CustomRequest.custom_request(method="GET", url=self.base_url + GET_USER_INFO)
        validate(instance=response.json(), schema=schema_user_info.valid_schema)
        return requests.ResponseModel(status=response.status_code, response=response.json())

    def api_users_list(self):
        """
            :return: Custom ResponseModel object with status and json with users list.
                For more information about ResponseModel obj check helpers.requests.
        """
        response = requests.CustomRequest.custom_request(method="GET", url=self.base_url + GET_USERS_LIST)
        validate(instance=response.json(), schema=schema_users_list.valid_schema)
        return requests.ResponseModel(status=response.status_code, response=response.json())

    def api_login(self):
        """
        :return: Custom ResponseModel object with status and json with auth token
        """
        response = requests.CustomRequest.custom_request(method="POST", url=self.base_url + POST_LOGIN, json=login_dict)
        validate(instance=response.json(), schema=schema_login.valid_schema)
        return requests.ResponseModel(status=response.status_code, response=response.json())
