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
    create_engine,
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    scoped_session,
    declared_attr,
)

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

DB_URL = "postgresql+pg8000://username:passwd!@localhost/blog"
DB_ASYNC_URL = "postgresql+asyncpg://username:passwd!@localhost/blog"
DB_ECHO = True


class Base:
    @declared_attr
    def __tablename__(cls):
        # users
        # posts
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


engine = create_engine(url=DB_URL, echo=DB_ECHO)
Base = declarative_base(bind=engine, cls=Base)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class User(Base):
    name = Column(String(50))
    username = Column(String(20), unique=True)
    email = Column(String(20), unique=True)

    # orm
    posts = relationship("Post", back_populates="user", uselist=True)

    def __str__(self):
        return f"User(id={self.id}, username={self.username!r})"


class Post(Base):
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(200), unique=False, nullable=False)
    body = Column(Text, nullable=False, default="")

    # orm
    user = relationship("User", back_populates="posts", uselist=False)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r})"

    def __repr__(self):
        return str(self)
