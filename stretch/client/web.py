import datetime
import logging
from typing import Dict

import requests

from stretch.api.v1.schema.token import Token

from .base import Method, StretchException, WebClient


class SyncWebClient(WebClient):
    def __init__(self, *args, **kwargs):
        super(SyncWebClient, self).__init__(*args, **kwargs)
        self._session = requests.Session()
        self._session.verify = self._ssl_verify

    def set_token(self, access_token, access_expire=None, refresh_token=None, refresh_expire=None, token_type="Bearer"):
        super(SyncWebClient, self).set_token(access_token, access_expire, refresh_token, refresh_expire, token_type)
        self._session.headers = self._default_headers

    def refresh(self):
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
            return True

    def check_and_update_token(self):
        if (
            isinstance(self._access_expire, datetime.datetime)
            and self._access_expire <= datetime.datetime.utcnow() < self._refresh_expire
        ):
            return self.refresh()

    def fetch(
        self,
        method: Method,
        url: str,
        params: Dict | None = None,
        data=None,
        json=None,
        headers=None,
        files=None,
        check=True,
    ):
        if self._profiling:
            _start = datetime.datetime.utcnow()
        if check:
            self.check_and_update_token()
        url = f"{self._base_url}{url}"
        response = None
        if method == Method.get:
            response = self._session.get(url, data=data, json=json, params=params, files=files, headers=headers)
        elif method == Method.post:
            response = self._session.post(url, data=data, json=json, params=params, files=files, headers=headers)
        elif method == Method.put:
            response = self._session.put(url, data=data, json=json, params=params, files=files, headers=headers)
        elif method == Method.delete:
            response = self._session.delete(url, data=data, json=json, params=params, files=files, headers=headers)
        elif method == Method.patch:
            response = self._session.patch(url, data=data, json=json, params=params, files=files, headers=headers)

        if response is not None and 200 <= response.status_code < 400:
            if self._profiling:
                logging.info(
                    f"[Request {method.value}] {(datetime.datetime.utcnow() - _start).microseconds/1000} ms url {url}"
                )
            return response.json()
        if response is not None:
            raise StretchException(response.status_code, response.json())

        raise StretchException(400, {"message": "Request method wrong", "error": "method-error"})
