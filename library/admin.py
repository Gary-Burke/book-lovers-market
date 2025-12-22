from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Lists message and read fields for display in admin
    """
    list_display = ("title", "author", "isbn", "status")
    search_fields = ["title", "author", "isbn", "status"]
    list_filter = ("title", "author", "isbn", "status")
    


# Register your models here.
