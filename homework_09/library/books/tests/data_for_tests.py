from books.models import Category, Book, Reader, BookOnHand
import datetime

category_str = "Русская классика"

category_header = "Информация о жанре"
book_header = "Информация о книге"
reader_header = "Информация о читателе"
bookonhand_header = "Книга у читателя"


def get_category():
    return Category.objects.create(name=category_str)


def get_book(category):
    return Book.objects.create(
        author="Тургенев Иван Сергеевич",
        name="Отцы и дети",
        category=category,
        publisher="Эксмо",
        year=2001,
        place='{"шкаф": 1, "полка": 3}',
        details="Помяты края",
    )


def get_reader():
    return Reader.objects.create(
        name="Сидоров Василий Петрович",
        address="Санкт-Петербург, ул.Войкова, д.1, кв.5",
        phone="+79351112233",
    )


def get_bookonhand(book, reader):
    return BookOnHand.objects.create(
        book=book, reader=reader, issuedate=datetime.date(2023, 1, 15)
    )
