import datetime
from typing import Dict

import requests
from stretch.api.v1.schema.token import Token

from .base import Method, StretchExceptions, WebClient


class SyncWebClient(WebClient):
    def __init__(self, *args, **kwargs):
        super(SyncWebClient, self).__init__(*args, **kwargs)
        self._session = requests.Session()

    def set_token(self, access_token, access_expire, refresh_token, refresh_expire, token_type="Bearer"):
        super(SyncWebClient, self).set_token(access_token, access_expire, refresh_token, refresh_expire, token_type)
        self._session.headers = self._default_headers

    def refresh(self):
        print("refresh token")
        if self._refresh_token is not None and self._refresh_url:
            headers = {
                "Authorization": f"Bearer {self._refresh_token}",
            }
            response = self.fetch(Method.post, self._refresh_url, headers=headers, json={}, check=False)
            token = Token(**response)
            self.set_token(
                access_token=token.access_token,
                access_expire=token.access_expire,
                refresh_token=token.refresh_token,
                refresh_expire=token.refresh_expire,
                token_type=token.token_type,
            )

            print("refresh token", token)
            return True

    def check_and_update_token(self):
        print("date expire:", self._access_expire, self._refresh_expire)
        print(isinstance(self._access_expire, datetime.datetime))
        if (
            isinstance(self._access_expire, datetime.datetime)
            and self._access_expire <= datetime.datetime.utcnow() < self._refresh_expire
        ):
            return self.refresh()

    def fetch(
        self, method: Method, url: str, params: Dict | None = None, data=None, json=None, headers=None, check=True
    ):
        if check:
            self.check_and_update_token()
        url = f"{self._base_url}{url}"
        # if headers is None:
        #    headers = self._default_headers
        # if isinstance(data, dict):
        #    data = urlencode(data)
        print(url)
        print(data, json, headers)
        response = None

        if method == Method.get:
            response = self._session.get(url, data=data, json=json, params=params, headers=headers)
        elif method == Method.post:
            response = self._session.post(url, data=data, json=json, params=params, headers=headers)

        if response is not None and 200 <= response.status_code < 400:
            return response.json()
        if response is not None:
            raise StretchExceptions(response.status_code, response.json())

        raise StretchExceptions(400, "Request method wrong")
