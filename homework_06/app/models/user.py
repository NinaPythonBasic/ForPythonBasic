from sqlalchemy import Column, Integer, String

from .database import db


class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, default="", server_default="")
    username = Column(
        String(30), nullable=False, unique=True, default="", server_default=""
    )
    email = Column(
        String(40), nullable=False, unique=True, default="", server_default=""
    )

    def __str__(self):
        return f"User(id={self.id}, username={self.username!r})"
