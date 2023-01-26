from django.test import TestCase
from books.tests.data_for_tests import (
    category_header,
    get_category,
)


class TestCategoryListView(TestCase):
    def test_response_status_code(self):
        response = self.client.get("/categories/")
        self.assertEqual(response.status_code, 200)

    def test_response_context(self):
        response = self.client.get("/categories/")
        self.assertIn("object_list", response.context)
        self.assertIn("category_list", response.context)

    def test_content(self):
        category = get_category()
        response = self.client.get("/categories/")
        href = f'<a  href="/category/{category.pk}/">'.encode(encoding="utf-8")
        self.assertIn(href, response.content)


class TestCategoryDetailView(TestCase):
    def test_response_unknown_page(self):
        # status_code
        response = self.client.get("/category/77/")
        self.assertEqual(response.status_code, 404)

    def test_response_known_page(self):
        category = get_category()
        # status_code
        response = self.client.get(f"/category/{category.pk}/")
        self.assertEqual(response.status_code, 200)
        # context
        self.assertIn("object", response.context)
        self.assertIn("category", response.context)
        # content
        header = category_header.encode(encoding="utf-8")
        self.assertIn(header, response.content)
