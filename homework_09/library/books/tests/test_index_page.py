from django.test import TestCase
from django.contrib.auth.models import User


class TestIndexView(TestCase):
    def test_guest_index_page(self):
        # status_code
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        # content
        hello = "Hello, Stranger!".encode(encoding="utf-8")
        self.assertIn(hello, response.content)

    def test_authorized_index_page(self):
        # create user
        username = "user"
        User.objects.create_user(
            username=username, email="user@email.com", password="user123456"
        )
        self.client.login(username=username, password="user123456")
        # authorized user
        # status_code
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        # content
        hello = f"Hello, {username}!".encode(encoding="utf-8")
        self.assertIn(hello, response.content)
        self.client.logout()

    def test_left_links(self):
        response = self.client.get("/")
        # content

        href_list = '<a href="/categories/">'.encode(encoding="utf-8")
        self.assertIn(href_list, response.content)

        href_list = '<a href="/books/">'.encode(encoding="utf-8")
        self.assertIn(href_list, response.content)

        href_list = '<a href="/readers/">'.encode(encoding="utf-8")
        self.assertIn(href_list, response.content)

        href_list = '<a href="/booksonhand/">'.encode(encoding="utf-8")
        self.assertIn(href_list, response.content)
