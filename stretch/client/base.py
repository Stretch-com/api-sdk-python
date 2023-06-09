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


class StretchException(Exception):
    def __init__(self, code=401, data=None):
        self.code = code
        self.data = data
        super(StretchException, self).__init__(f"Request exception: [{code}] {data}")

    def errors(self):
        if self.code == 422 and self.data["error"] == "validation-error":
            return {efl["field"]: efl["message"] for efl in self.data["fields"]}
        return {}


class WebClient(ABC):
    def __init__(
        self,
        client_id: str,
        client_secret: str = "",
        base_url: str = "https://api.stretch.com/api/v1",
        refresh_url: str = "/auth/refresh",
        profiling: bool = False,
        ssl_verify: bool = True,
    ):
        self._user_id = None
        self._ssl_verify = ssl_verify
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

    def set_token(self, access_token, access_expire=None, refresh_token=None, refresh_expire=None, token_type="Bearer"):
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
        if self._default_headers is None:
            self._default_headers = {}
        self._default_headers["Authorization"] = f"{token_type} {self._access_token}"

    def set_user(self, user_id):
        self._user_id = user_id
        if self._user_id is not None:
            if self._default_headers is None:
                self._default_headers = {}
            self._default_headers["Authorization-User"] = self._user_id

    @property
    def basic(self):
        return self._basic

    @abstractmethod
    def fetch(
        self, method: Method, url: str, params: Dict | None = None, data=None, json=None, files=None, headers=None
    ):
        pass
