from .base import ApiBase
from stretch.client.base import Method
from urllib.parse import urlparse
import requests


class Storage(ApiBase):
    """
    Auth Stretch API
    """

    def _get_file_stream(self, filename):
        if isinstance(filename, str):
            url = urlparse(filename)
            if url.scheme in ["http", "https"]:
                r = requests.get(filename, allow_redirects=True)
                filestream = r.content
            else:
                filestream = open(filename, "rb")
                # filestream = filestream.read()
        else:
            filestream = filename
            filename = "stream"
        return filename, filestream, "image/jpg"

    def post_avatar(self, filename):
        """
        Upload avatar
        """
        return self._fetch(Method.post, "/storage/profile/avatar", files={"file": self._get_file_stream(filename)})

    def post_image(self, filename, title: str = None):
        """
        Upload avatar
        """
        data = None
        if title is not None:
            data = {"title": title}
        return self._fetch(Method.post, "/storage/image", data=data, files={"file": self._get_file_stream(filename)})
