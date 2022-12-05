"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import (
    sessionmaker,
    declarative_base,
    declared_attr,
)

DB_ASYNC_URL = "postgresql+asyncpg://postgres:password@localhost/postgres"
DB_ECHO = True
PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or DB_ASYNC_URL


class Base:
    @declared_attr
    def __tablename__(cls):
        # users
        # posts
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


engine: AsyncEngine = create_async_engine(
    url=PG_CONN_URI,
    echo=DB_ECHO,
)
Base = declarative_base(bind=engine, cls=Base)

Session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class User(Base):
    name = Column(String(50))
    username = Column(String(30), unique=True)
    email = Column(String(40), unique=True)

    # orm
    posts = relationship("Post", back_populates="user", uselist=True)

    def __str__(self):
        return f"User(id={self.id}, username={self.username!r})"


class Post(Base):
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(
        String(300),
        unique=False,
        nullable=False,
        default="",
        server_default=""
    )
    body = Column(Text, nullable=False, default="", server_default="")

    # orm
    user = relationship("User", back_populates="posts", uselist=False)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r})"

    def __repr__(self):
        return str(self)
