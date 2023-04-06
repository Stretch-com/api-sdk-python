from .base import ApiBase
from .schema.token import Token
from typing import Awaitable, Union
from stretch.client.base import Method


class Search(ApiBase):
    """
    Auth Stretch API
    """

    def get_filter(self, **kwargs):
        """
        Get filter information
        """
        return self._fetch(Method.get, "/search/filter", json=kwargs)

    def post(self, **kwargs):
        """
        Get filter information
        """
        return self._fetch(Method.post, "/search", json=kwargs)
