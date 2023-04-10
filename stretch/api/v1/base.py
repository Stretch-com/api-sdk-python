from typing import Any, Dict, List, Union

from stretch.client.base import Method


class ResponseStruct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

    def __repr__(self) -> str:
        return "{ " + ", ".join(f"{k} = {v}" for k, v in self.dict().items()) + " }"

    def dict(self) -> dict:
        return self.__dict__


class ApiBase:
    def __init__(self, core):
        self._core = core

    def _fetch(
        self, method: Method, url, params=None, data=None, json=None, headers=None, files=None, model=None
    ) -> Union[ResponseStruct, List[ResponseStruct], Any]:
        response = self._core.provider.fetch(
            method, url, params=params, data=data, json=json, files=files, headers=headers
        )
        if model is not None:
            return model.create(**response)
        else:
            if isinstance(response, Dict):
                return ResponseStruct(**response)
            elif isinstance(response, List):
                return [ResponseStruct(**it) for it in response]
            else:
                return response
