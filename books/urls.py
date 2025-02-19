from django.urls import path

from books.views import book_list, book_create, update_book_details, book_detail, book_delete, book_status_change

urlpatterns = [
    path("", book_list, name="book_list"),
    path("create_book/", book_create, name="create_book"),
    path("update_book_details/<int:pk>/", update_book_details, name="update_book_details"),
    path("book_detail/<int:pk>/", book_detail, name="book_detail"),
    path("delete_book/<int:pk>/", book_delete, name="delete_book"),
    path("update_book_status/<int:pk>/", book_status_change, name="update_book_status"),
]