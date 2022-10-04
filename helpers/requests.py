import requests


class CustomRequest:
    @staticmethod
    def custom_request(method: str, url: str, **kwargs):
        """
                Method for the new Request object: GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE.
                url – URL for the new Request object.
                **kwargs:
                    params – (optional) Dictionary, list of tuples or bytes to send in the query string for the Request.
                    json – (optional) A JSON serializable Python object to send in the body of the Request.
                    headers – (optional) Dictionary of HTTP Headers to send with the Request.
        """
        return requests.request(method, url, **kwargs)


class ResponseModel:
    def __init__(self, status: int, response: dict = None):
        self.status = status
        self.response = response
