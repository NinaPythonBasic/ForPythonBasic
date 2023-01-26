from django.shortcuts import render

from books.models import Book


def main_page(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "books/index.html", context)
