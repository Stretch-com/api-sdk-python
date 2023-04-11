from .base import Base
from dataclasses import dataclass # fix


@dataclass()
class Token(Base):
    access_token: str | None = None
    refresh_token: str | None = None
    token_type: str | None = None
    access_expire: int | None = None
    refresh_expire: int | None = None
