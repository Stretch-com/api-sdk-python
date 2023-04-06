import urllib

from stretch.api.v1.auth import Auth
from .client.web import SyncWebClient


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
        self._provider = SyncWebClient(client_id=client_id, client_secret=client_secret, base_url=self._api_url)
        self.auth = Auth(self)
        print(dir(self._api))

    @property
    def provider(self):
        return self._provider
