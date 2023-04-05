from dataclasses import dataclass, fields
import inspect


class Base:
    @classmethod
    def create(cls, **kwargs):
        return cls(**{k: v for k, v in kwargs.items() if k in inspect.signature(cls).parameters})
