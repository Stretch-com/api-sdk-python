from dataclasses import dataclass

from .base import Base


@dataclass()
class Token(Base):
    access_token: str | None = None
    refresh_token: str | None = None
    token_type: str | None = None
    access_expire: int | None = None
    refresh_expire: int | None = None
