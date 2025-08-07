import httpx


class TokenAuth(httpx.Auth):
    """
    HTTP authentication using NetBox API tokens.
    """

    def __init__(self, token):
        self.token = token

    def auth_flow(self, request):
        request.headers["Authorization"] = f"Token {self.token}"
        yield request
