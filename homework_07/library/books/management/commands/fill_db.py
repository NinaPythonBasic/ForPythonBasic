from django.core.management.base import BaseCommand
from books.models import Category, Book, Reader, BookOnHand

import datetime


class Command(BaseCommand):
    help = "Fill db"

    def handle(self, *args, **options):
        print("Удаляем старые данные")
        BookOnHand.objects.all().delete()
        Reader.objects.all().delete()
        Book.objects.all().delete()
        Category.objects.all().delete()

        print("Создаем новые данные")
        rus_category = Category.objects.create(name="Русская классика")
        foreign_category = Category.objects.create(name="Зарубежная классика")

        book1 = Book.objects.create(
            author="Тургенев Иван Сергеевич",
            name="Отцы и дети",
            category=rus_category,
            publisher="Эксмо",
            year=2001,
            place='{"шкаф": 1, "полка": 3}',
            details="Помяты края",
        )

        book2 = Book.objects.create(
            author="Булгаков Михаил Афанасьевич",
            name="Мастер и Маргарита",
            category=rus_category,
            publisher="АСТ",
            year=2006,
            place='{"шкаф": 2, "полка": 2}',
        )

        book3 = Book.objects.create(
            author="Лондон Джек",
            name="Мартин Иден",
            category=foreign_category,
            publisher="Азбука",
            year=2007,
            place='{"шкаф": 3, "полка": 1}',
        )

        reader1 = Reader.objects.create(
            name="Сидоров Василий Петрович",
            address="Санкт-Петербург, ул.Войкова, д.1, кв.5",
            phone="+79351112233",
        )

        reader2 = Reader.objects.create(
            name="Иванов Савелий Иванович",
            address="Санкт-Петербург, ул.Ботаническая, д.2, кв.13",
            phone="+79351112234",
        )

        bookonhand = BookOnHand.objects.create(
            book=book3, reader=reader2, issuedate=datetime.date(2022, 12, 30)
        )

        book3.onhand = True
        book3.save()
