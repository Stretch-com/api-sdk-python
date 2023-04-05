from abc import ABC, abstractmethod
from typing import Dict


class WebClient(ABC):
    @abstractmethod
    def get(self, url: str, query_params: Dict | None = None):
        pass

    @abstractmethod
    def post(self, url: str, query_params: Dict | None = None, body=None, json=None, content_type=None):
        pass

    @abstractmethod
    def put(self, query_params: Dict | None = None, body=None, json=None, content_type=None):
        pass

    @abstractmethod
    def patch(self, query_params: Dict | None = None, body=None, json=None, content_type=None):
        pass

    @abstractmethod
    def delete(self, query_params: Dict | None = None, body=None, json=None, content_type=None):
        pass
