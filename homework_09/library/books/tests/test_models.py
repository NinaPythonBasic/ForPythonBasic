from django.test import TestCase
from books.models import Category, Book, Reader
from books.tests.data_for_tests import (
    category_str,
    get_category,
    get_book,
    get_reader,
    get_bookonhand,
)
import datetime


class TestCategory(TestCase):
    def setUp(self) -> None:
        self.category = get_category()

    def tearDown(self) -> None:
        self.category.delete()

    def test_init(self):
        self.assertTrue(isinstance(self.category.name, str))
        self.assertEqual(self.category.name, category_str)

    def test_str(self):
        self.assertEqual(str(self.category), category_str)

    def test_repr(self):
        self.assertEqual(repr(self.category), category_str)


class TestBook(TestCase):
    def setUp(self) -> None:
        self.category = get_category()
        self.book = get_book(self.category)

    def tearDown(self) -> None:
        self.book.delete()
        self.category.delete()

    def test_fields_type(self):
        self.assertTrue(isinstance(self.book.author, str))
        self.assertTrue(isinstance(self.book.name, str))
        self.assertTrue(isinstance(self.book.category, Category))
        self.assertTrue(isinstance(self.book.publisher, str))
        self.assertTrue(isinstance(self.book.year, int))
        self.assertTrue(isinstance(self.book.place, str))
        self.assertTrue(isinstance(self.book.details, str))

    def test_str(self):
        self.assertEqual(str(self.book), f"{self.book.name} ({self.book.author})")

    def test_raises(self):
        with self.assertRaises(Exception):
            get_book("Какая-то категория")


class TestReader(TestCase):
    def setUp(self) -> None:
        self.reader = get_reader()

    def tearDown(self) -> None:
        self.reader.delete()

    def test_fields_type(self):
        self.assertTrue(isinstance(self.reader.name, str))
        self.assertTrue(isinstance(self.reader.address, str))
        self.assertTrue(isinstance(self.reader.phone, str))


class TestBookOnHand(TestCase):
    def setUp(self) -> None:
        self.category = get_category()
        self.book = get_book(self.category)
        self.reader = get_reader()
        self.bookonhand = get_bookonhand(self.book, self.reader)

    def tearDown(self) -> None:
        self.bookonhand.delete()
        self.reader.delete()
        self.book.delete()
        self.category.delete()

    def test_fields_type(self):
        self.assertTrue(isinstance(self.bookonhand.book, Book))
        self.assertTrue(isinstance(self.bookonhand.reader, Reader))
        self.assertTrue(isinstance(self.bookonhand.issuedate, datetime.date))
        self.assertIsNone(self.bookonhand.returndate)
        self.assertTrue(isinstance(self.bookonhand.details, str))
