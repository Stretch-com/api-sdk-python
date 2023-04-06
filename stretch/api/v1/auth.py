from .base import ApiBase
from .schema.token import Token
from typing import Awaitable, Union
from stretch.client.base import Method


class Auth(ApiBase):
    """
    Auth Stretch API
    """

    def login(self, username: str, password: str) -> bool:
        """
        Login to platform under account
        """
        response = self.token(username, password)
        return response.access_token is not None

    def guest(self):
        """
        Login as guest account ( client role )
        """
        response = self.post_guest()
        return response.access_token is not None

    def get_user(self):
        """
        Get user information
        """
        return self._fetch(Method.get, "/auth/user")

    def put_user(self, **kwargs):
        """
        Update user information
        """
        return self._fetch(Method.put, "/auth/user", json=kwargs)

    def post_guest(self, auto_save: bool = True):
        headers = {
            "Authorization": f"Basic {self._core.provider.basic}",
        }
        data = {"grant_type": "create"}
        response: Token = self._fetch(Method.post, "/auth/guest", json=data, headers=headers, model=Token)
        return self._update_token(response, auto_save)

    def post_signup(self, phone: str, type: str = "client", auto_save=True):
        headers = {
            "Authorization": f"Basic {self._core.provider.basic}",
        }
        data = {"grant_type": "create", "phone": phone, "type": type}
        response: Token = self._fetch(Method.post, "/auth/signup", json=data, headers=headers, model=Token)
        return self._update_token(response, auto_save)

    def token(
        self, username: str, password: str, scope: str = None, auto_save: bool = True
    ) -> Union[Token, Awaitable[Token]]:
        """
        Get auth token from
        """
        headers = {
            "Authorization": f"Basic {self._core.provider.basic}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {"grant_type": "password", "username": username, "password": password}
        if scope is not None:
            data["scope"] = scope

        response: Token = self._fetch(Method.post, "/auth/token", data=data, headers=headers, model=Token)
        return self._update_token(response, auto_save)

    def _update_token(self, response: Token, auto_save=False):
        if auto_save:
            self._core.provider.set_token(
                access_token=response.access_token,
                access_expire=response.access_expire,
                refresh_token=response.refresh_token,
                refresh_expire=response.refresh_expire,
                token_type=response.token_type,
            )
        return response
