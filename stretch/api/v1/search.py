from stretch.client.base import Method

from .base import ApiBase


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
