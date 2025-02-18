from django.contrib import admin

from books.models import Books


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price", "read")


admin.site.register(Books, BookAdmin)
