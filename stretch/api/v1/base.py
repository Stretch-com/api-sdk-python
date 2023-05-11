import asyncio
import functools

# import logging
from re import sub
from typing import Any, Dict, List, Union

from stretch.client.aioweb import AsyncWebClient
from stretch.client.base import Method


class ResponseStruct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

    def __repr__(self) -> str:
        return "{ " + ", ".join(f"{k}={v}" for k, v in self.dict().items()) + " }"

    def __getattr__(self, item):
        s = sub(r"(_|-)+", " ", item).title().replace(" ", "")
        if len(s) > 1:
            camel_case = "".join([s[0].lower(), s[1:]])
            if camel_case in self.__dict__:
                return getattr(self, camel_case)
        raise AttributeError(
            f"Stretch API Response don't have property '{item}' check list: {', '.join(self.__dict__.keys())}"
        )

    def dict(self) -> dict:
        return self.__dict__


def api_decoration_func(fn):
    def api_decoration_func_wrapper(*args, **kwargs):
        if isinstance(args[0]._core.provider, AsyncWebClient):
            try:
                loop = asyncio.get_running_loop()
                fnp = functools.partial(fn, *args, **kwargs)
                return loop.run_in_executor(None, fnp)
            except Exception:
                pass

        return fn(*args, **kwargs)

    return api_decoration_func_wrapper


def for_all_methods(decorator):
    def decorate(cls):
        for attr in cls.__dict__:  # there's propably a better way to do this
            if callable(getattr(cls, attr)):
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls

    return decorate


class ApiBase:
    def __init__(self, core):
        self._core = core

    def _fetch(
        self, method: Method, url, params=None, data=None, json=None, headers=None, files=None, model=None
    ) -> Union[ResponseStruct, List[ResponseStruct], Any]:
        response = self._core.provider.fetch(
            method, url, params=params, data=data, json=json, files=files, headers=headers, check=self._core._check
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
