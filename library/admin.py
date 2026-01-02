from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Lists the title, author, isbn, status and price fields for display in admin
    """
    list_display = ("title", "author", "isbn", "status", "price")
    search_fields = ["title", "author", "isbn"]
    list_filter = ("status",)


# Register your models here.
