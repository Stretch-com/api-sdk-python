from copy import copy

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
        self,
        client_id,
        client_secret=None,
        base_url="https://api.stretch.com",
        api_version=1,
        profiling=False,
        ssl_verify=True,
        provider=SyncWebClient,
    ):
        self._user_id = None
        self._access_token = None
        self._api_url = f"{base_url}/api/v{api_version}"
        self._api = __import__(f"stretch.api.v{api_version}")
        self._client_id = client_id
        self._client_secret = client_secret
        self._provider = provider(
            client_id=client_id,
            client_secret=client_secret,
            base_url=self._api_url,
            profiling=profiling,
            ssl_verify=ssl_verify,
        )
        self._check = True
        self.auth = Auth(self)
        self.coach = Coach(self)
        self.nav = Nav(self)
        self.search = Search(self)
        self.storage = Storage(self)

    @property
    def provider(self):
        return self._provider

    def __call__(self, *args, **kwargs):
        obj = copy(self)
        if "user_id" in kwargs:
            obj._user_id = kwargs["user_id"]
            obj._provider.set_user(obj._user_id)
        if "access_token" in kwargs:
            self._check = False
            obj._access_token = kwargs["access_token"]
            if "access_expire" in kwargs:
                access_expire = kwargs["access_expire"]
            else:
                access_expire = 120

            obj._provider.set_token(access_token=obj._access_token, access_expire=access_expire)
            obj._provider._access_expire = None
        return obj
