import base64
import datetime
from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict


class Method(str, Enum):
    post = "post"
    get = "get"
    put = "put"
    patch = "patch"
    delete = "delete"


class StretchExceptions(Exception):
    def __init__(self, code=401, data=None):
        super(StretchExceptions, self).__init__(f"Request exception: [{code}] {data}")


class WebClient(ABC):
    def __init__(
        self,
        client_id: str,
        client_secret: str = "",
        base_url: str = "https://api.stretch.com/api/v1",
        refresh_url: str = "/auth/refresh",
        profiling: bool = False,
    ):
        self._refresh_expire = None
        self._refresh_token = None
        self._access_expire = None
        self._access_token = None
        self._profiling = profiling
        self._base_url = base_url
        self._refresh_url = refresh_url
        if client_secret is None:
            client_secret = ""
        self._basic = base64.b64encode(f"{client_id}:{client_secret}".encode("latin1")).decode("ascii").strip()
        self._default_headers = None

    def set_token(self, access_token, access_expire, refresh_token, refresh_expire, token_type="Bearer"):
        if access_token is not None:
            self._access_token = access_token
        if access_expire is not None:
            self._access_expire = (
                datetime.datetime.utcnow() + datetime.timedelta(seconds=access_expire) - datetime.timedelta(seconds=30)
            )
        if refresh_token is not None:
            self._refresh_token = refresh_token
        if refresh_expire is not None:
            self._refresh_expire = (
                datetime.datetime.utcnow() + datetime.timedelta(seconds=refresh_expire) - datetime.timedelta(seconds=30)
            )

        self._default_headers = {
            "Authorization": f"{token_type} {self._access_token}",
            "Content-Type": "application/json",
        }

    @property
    def basic(self):
        return self._basic

    @abstractmethod
    def fetch(self, method: Method, url: str, params: Dict | None = None, data=None, json=None, headers=None):
        pass
