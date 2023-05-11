from urllib.parse import urlparse

import requests

from stretch.client.base import Method

from .base import ApiBase, api_decoration_func, for_all_methods


@for_all_methods(api_decoration_func)
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

        return filename, filestream, "image/jpeg"

    def post_avatar(self, filename):
        """
        Upload avatar
        """
        return self._fetch(
            Method.post,
            "/storage/profile/avatar",
            files={"file": self._get_file_stream(filename)},
        )

    def post_image(self, filename, title: str = None):
        """
        Upload image to gallery
        """
        data = None
        if title is not None:
            data = {"title": title}
        return self._fetch(Method.post, "/storage/image", json=data, files={"file": self._get_file_stream(filename)})

    def post_certificate(self, filename, title: str = None, description: str = None):
        """
        Upload certificate
        """
        data = None
        if title is not None:
            data = {"title": title}
            if description is not None:
                data["description"] = description
        return self._fetch(
            Method.post, "/storage/certificate", json=data, files={"file": self._get_file_stream(filename)}
        )
