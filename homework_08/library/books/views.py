from django.shortcuts import render
from django.views.generic import ListView, DetailView

from books.models import Book, Category, Reader, BookOnHand


def main_page(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "books/index.html", context)


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category


class ReaderListView(ListView):
    model = Reader


class ReaderDetailView(DetailView):
    model = Reader


class BookOnHandListView(ListView):
    model = BookOnHand


class BookOnHandDetailView(DetailView):
    model = BookOnHand
