from __future__ import annotations

from datetime import datetime, timedelta

from sqlalchemy import Integer, ForeignKey, Column, Text
from sqlalchemy.orm import relationship, Mapped

from app import db
from config import Config
from database.models.base import Base
from helpers.helpers import generate_token


class Users(db.Model, Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    role_id: Mapped[int] = Column(ForeignKey("roles.id"))
    role: Mapped["Roles"] = relationship(back_populates="users")  # noqa
    username = Column(Text, nullable=False)
    password = Column(Text, nullable=False)

    access_token = Column(Text)
    token_updated = Column(Integer)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "role": self.role.name,
            "can_delete": self.role.can_delete,
            "username": self.username,
            "token_valid": self.token_expire.timestamp() > self.token_updated,
            "token_updated": datetime.fromtimestamp(self.token_updated),
            "token_expire": self.token_expire,
        }

    def create_token(self) -> str:
        self.access_token = generate_token(150)
        self.token_updated = datetime.now().timestamp()
        self.commit()
        return self.access_token

    def clear_token(self) -> None:
        self.access_token = None
        self.access_token = None
        self.commit()

    @property
    def is_token_expired(self):
        if not self.token_updated:
            return True
        token_time = datetime.fromtimestamp(self.token_updated)
        time_diff = (datetime.now() - token_time).total_seconds() / 60
        return time_diff > Config.API_EXPIRE_MIN

    @property
    def token_expire(self):
        if not self.token_updated:
            return None
        token_time = datetime.fromtimestamp(self.token_updated)
        return token_time + timedelta(minutes=Config.API_EXPIRE_MIN)

    @classmethod
    def filter_by(cls, **kwargs) -> Users:
        return super().filter_by(**kwargs).first()
