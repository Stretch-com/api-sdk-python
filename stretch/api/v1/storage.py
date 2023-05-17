import logging
from urllib.parse import urlparse
from uuid import UUID

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

    def get_images(self, **kwargs):
        """
        Get certificates
        """
        return self._fetch(Method.get, f"/storage/images", json=kwargs)

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

    def put_image(self, image_id: UUID, file=None, filename=None, **kwargs):
        """
        Upload certificate
        """
        if file is not None:
            files = {"file": self._get_file_stream(file, filename)}
        else:
            files = None
        return self._fetch(Method.put, f"/storage/image/{image_id}", json=kwargs, files=files)

    def delete_image(self, image_id: UUID, **kwargs):
        """
        Delete certificate
        """
        return self._fetch(Method.delete, f"/storage/image/{image_id}", json=kwargs)

    def get_certificates(self, **kwargs):
        """
        Get certificates
        """
        return self._fetch(Method.get, f"/storage/certificates", json=kwargs)

    def post_certificate(self, file, filename=None, **kwargs):
        """
        Upload certificate
        """
        return self._fetch(
            Method.post, "/storage/certificate", json=kwargs, files={"file": self._get_file_stream(file, filename)}
        )

    def put_certificate(self, certificate_id: UUID, file=None, filename=None, **kwargs):
        """
        Upload certificate
        """
        if file is not None:
            files = {"file": self._get_file_stream(file, filename)}
        else:
            files = None
        return self._fetch(Method.put, f"/storage/certificate/{certificate_id}", data=kwargs, files=files)

    def delete_certificate(self, certificate_id: UUID, **kwargs):
        """
        Delete certificate
        """
        return self._fetch(Method.delete, f"/storage/certificate/{certificate_id}", json=kwargs)
