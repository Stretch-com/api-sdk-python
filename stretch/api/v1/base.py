from stretch.client.base import Method


class ApiBase:
    def __init__(self, core):
        self._core = core

    def _fetch(self, method: Method, url, params=None, data=None, json=None, headers=None, model=None):
        response = self._core.provider.fetch(method, url, params=params, data=data, json=json, headers=headers)
        if model is not None:
            return model.create(**response)
        else:
            return response
