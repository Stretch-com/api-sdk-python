import urllib

from stretch.api.v1.auth import Auth


class Stretch:
    """
    Python API Stretch SDK main class
    """

    auth: Auth = None

    def __init__(self, client_id, client_secret=None, base_url="https://api.stretch.com", api_version=1):
        self._api_url = f"{base_url}/api/v{api_version}"
        self._api = __import__(f"stretch.api.v{api_version}")
        self._client_id = client_id
        self._client_secret = client_secret
        self.auth = Auth(self)
        print(dir(self._api))
