from .base import ApiBase
from stretch.client.base import Method


class Storage(ApiBase):
    """
    Auth Stretch API
    """

    def avatar(self, filename):
        """
        Upload avatar
        """
        if isinstance(filename, str):
            filestream = open(filename, "rb")
        else:
            filestream = filename
            filename = "stream"
        return self._fetch(Method.post, "/storage/profile/avatar", files={"file": (filename, filestream, "image/jpeg")})

    def post(self, **kwargs):
        """
        Get filter information
        """
        return self._fetch(Method.post, "/search", json=kwargs)
