from django.test import TestCase
from books.tests.data_for_tests import (
    reader_header,
    get_reader,
)


class TestReaderListView(TestCase):
    def test_response_status_code(self):
        response = self.client.get("/readers/")
        self.assertEqual(response.status_code, 200)

    def test_response_context(self):
        response = self.client.get("/readers/")
        self.assertIn("object_list", response.context)
        self.assertIn("reader_list", response.context)

    def test_content(self):
        reader = get_reader()
        response = self.client.get("/readers/")
        href = f'<a  href="/reader/{reader.pk}/">'.encode(encoding="utf-8")
        self.assertIn(href, response.content)


class TestReaderDetailView(TestCase):
    def test_response_unknown_page(self):
        # status_code
        response = self.client.get("/reader/77/")
        self.assertEqual(response.status_code, 404)

    def test_response_known_page(self):
        reader = get_reader()
        # status_code
        response = self.client.get(f"/reader/{reader.pk}/")
        self.assertEqual(response.status_code, 200)
        # context
        self.assertIn("object", response.context)
        self.assertIn("reader", response.context)
        # content
        header = reader_header.encode(encoding="utf-8")
        self.assertIn(header, response.content)
