from django.contrib import admin

from books.models import Book, BookOnHand, Reader, Category

admin.site.register(Book)
admin.site.register(BookOnHand)
admin.site.register(Reader)
admin.site.register(Category)
