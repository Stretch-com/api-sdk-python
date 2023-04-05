from .base import Base, dataclass


@dataclass()
class Token(Base):
    access_token: str | None = None
    refresh_token: str | None = None
    token_type: str | None = None
