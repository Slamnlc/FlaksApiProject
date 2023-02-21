from typing import List

from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship, Mapped

from app import db
from database.models.base import Base


class Roles(db.Model, Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    can_delete = db.Column(db.Boolean, default=False)
    users: Mapped[List["Users"]] = relationship(back_populates="role") # noqa
