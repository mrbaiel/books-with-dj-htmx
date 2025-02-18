from django.urls import path

from books.views import book_list, book_create

urlpatterns = [
    path('', book_list, name='book_list'),
    path('book_create/',book_create, name='book_create'),
]