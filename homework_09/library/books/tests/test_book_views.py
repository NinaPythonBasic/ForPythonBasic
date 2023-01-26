from django.test import TestCase
from books.tests.data_for_tests import (
    book_header,
    get_category,
    get_book,
)


class TestBookListView(TestCase):
    def test_response_status_code(self):
        response = self.client.get("/books/")
        self.assertEqual(response.status_code, 200)

    def test_response_context(self):
        response = self.client.get("/books/")
        self.assertIn("object_list", response.context)
        self.assertIn("book_list", response.context)

    def test_content(self):
        book = get_book(get_category())
        response = self.client.get("/books/")
        href = f'<a  href="/book/{book.pk}/">'.encode(encoding="utf-8")
        self.assertIn(href, response.content)


class TestBookDetailView(TestCase):
    def test_response_unknown_page(self):
        # status_code
        response = self.client.get("/book/77/")
        self.assertEqual(response.status_code, 404)

    def test_response_known_page(self):
        book = get_book(get_category())
        # status_code
        response = self.client.get(f"/book/{book.pk}/")
        self.assertEqual(response.status_code, 200)
        # context
        self.assertIn("object", response.context)
        self.assertIn("book", response.context)
        # content
        header = book_header.encode(encoding="utf-8")
        self.assertIn(header, response.content)
