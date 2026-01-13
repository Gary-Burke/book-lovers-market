from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Lists the title, author, isbn, status, price and user fields
    for display in admin
    """
    list_display = ("title", "author", "isbn", "status", "price", "user")
    search_fields = ["title", "author", "isbn", "user"]
    list_filter = ("status",)


# Register your models here.
