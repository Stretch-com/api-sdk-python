from .base import ApiBase
from .schema.token import Token
from typing import Awaitable, Union


class Auth(ApiBase):
    """
    Auth Stretch API
    """

    def token(self, username: str, password: str, auto_save: bool = True) -> Union[Token, Awaitable[Token]]:
        """
        Get auth token from
        """
        print(f"Auth f: {username} {password} {auto_save}")
        t = Token.create(access_token="sdssdfdfdsdfs", dsfksdfds=232234324)
        print(t, t.access_token)
        return t

    def guest(self):
        return
