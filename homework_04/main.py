"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker

from jsonplaceholder_requests import (
    fetch_users_data,
    fetch_posts_data
)

from models import (
    Base,
    User,
    Post,
    DB_ASYNC_URL,
    DB_ECHO
)

async_engine: AsyncEngine = create_async_engine(
    url=DB_ASYNC_URL,
    echo=DB_ECHO,
)

async_session = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_user(session: AsyncSession, username: str, email: str) -> User:
    user = User(username=username, email=email)
    session.add(user)
    print("user create", user)
    await session.commit()
    return user


async def create_posts_for_user(
    session: AsyncSession,
    user: User,
    *posts_titles: str,
) -> list[Post]:
    posts = [
        Post(title=post_title, user=user)
        for post_title in posts_titles
    ]
    session.add_all(posts)
    await session.commit()
    print("created posts", posts)

    return posts


async def create_users(
    session: AsyncSession,
    users_data: list[dict],
) -> list[User]:
    users = [
        User(
            id=user_data["id"],
            name=user_data["name"],
            username=user_data["username"],
            email=user_data["email"]
        )
        for user_data in users_data
    ]
    session.add_all(users)
    await session.commit()
    print("created users", users)

    return users


async def get_user_by_id(session: AsyncSession, user_id: int) -> User | None:
    user: User | None = await session.get(User, user_id)

    return user


async def create_posts(
    session: AsyncSession,
    posts_data: list[dict],
) -> list[User]:
    posts = []
    for post_data in posts_data:
        user: User | None = await get_user_by_id(session, post_data["userId"])
        if user is None:
            break
        post = Post(
            id=post_data["id"],
            user_id=1,
            title=post_data["title"],
            body=post_data["body"],
            user=user
        )
        posts.append(post)
        session.add(post)

    session.add_all(posts)
    await session.commit()
    print("created posts", posts)

    return posts


async def async_main():
    users_data: List[dict]
    posts_data: List[dict]

    await create_tables()

    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )

    async with async_session() as session:
        await create_users(session, users_data)
        await create_posts(session, posts_data)

if __name__ == "__main__":
    asyncio.run(async_main())
