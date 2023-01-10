"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from books import views

urlpatterns = [
    path("", views.main_page),
    path("books/", views.BookListView.as_view(), name="books"),
    path("categories/", views.CategoryListView.as_view(), name="categories"),
    path("readers/", views.ReaderListView.as_view(), name="readers"),
    path("booksonhand/", views.BookOnHandListView.as_view(), name="booksonhand"),
    path("book/<int:pk>/", views.BookDetailView.as_view(), name="book"),
    path("category/<int:pk>/", views.CategoryDetailView.as_view(), name="category"),
    path("reader/<int:pk>/", views.ReaderDetailView.as_view(), name="reader"),
    path(
        "bookonhand/<int:pk>/", views.BookOnHandDetailView.as_view(), name="bookonhand"
    ),
    path("admin/", admin.site.urls),
]
