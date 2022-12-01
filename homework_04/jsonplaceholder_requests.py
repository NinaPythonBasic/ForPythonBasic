"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        json_list = await response.json()

        return json_list


async def fetch_users_data():
    users_data =  await fetch_json(USERS_DATA_URL)

    return users_data


async def fetch_posts_data():
    posts_data = await fetch_json(POSTS_DATA_URL)

    return posts_data
