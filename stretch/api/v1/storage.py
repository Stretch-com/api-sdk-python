import logging
from urllib.parse import urlparse

import requests

from stretch.client.base import Method

from .base import ApiBase, api_decoration_func, for_all_methods


@for_all_methods(api_decoration_func)
class Storage(ApiBase):
    """
    Auth Stretch API
    """

    def _get_file_stream(self, file, filename=None):
        if isinstance(file, str):
            url = urlparse(file)
            if url.scheme in ["http", "https"]:
                r = requests.get(file, allow_redirects=True)
                filestream = r.content
            else:
                filestream = open(file, "rb")
                # filestream = filestream.read()
        else:
            filestream = file
            filename = filename if filename else "stream"

        logging.info(f"File stream: {filename} : {filestream}")

        return filename, filestream, "image/jpeg"

    def post_avatar(self, file, filename=None):
        """
        Upload avatar
        """
        return self._fetch(
            Method.post,
            "/storage/profile/avatar",
            files={"file": self._get_file_stream(file, filename)},
        )

    def post_image(self, file, title: str = None, filename=None):
        """
        Upload image to gallery
        """
        data = None
        if title is not None:
            data = {"title": title}
        return self._fetch(
            Method.post, "/storage/image", json=data, files={"file": self._get_file_stream(file, filename)}
        )

    def post_certificate(self, file, title: str = None, description: str = None, filename=None):
        """
        Upload certificate
        """
        data = None
        if title is not None:
            data = {"title": title}
            if description is not None:
                data["description"] = description
        return self._fetch(
            Method.post, "/storage/certificate", json=data, files={"file": self._get_file_stream(file, filename)}
        )
