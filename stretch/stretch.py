from stretch.api.v1.auth import Auth
from stretch.api.v1.coach import Coach
from stretch.api.v1.nav import Nav
from stretch.api.v1.search import Search
from stretch.api.v1.storage import Storage

from .client.web import SyncWebClient


class Stretch:
    """
    Python API Stretch SDK main class
    """

    auth: Auth = None
    search: Search = None
    storage: Storage = None

    def __init__(
        self, client_id, client_secret=None, base_url="https://api.stretch.com", api_version=1, profiling=False
    ):
        self._api_url = f"{base_url}/api/v{api_version}"
        self._api = __import__(f"stretch.api.v{api_version}")
        self._client_id = client_id
        self._client_secret = client_secret
        self._provider = SyncWebClient(
            client_id=client_id, client_secret=client_secret, base_url=self._api_url, profiling=profiling
        )
        self.auth = Auth(self)
        self.coach = Coach(self)
        self.nav = Nav(self)
        self.search = Search(self)
        self.storage = Storage(self)

    @property
    def provider(self):
        return self._provider
