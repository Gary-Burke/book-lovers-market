from django.contrib import admin
from .models import Home, Feedback


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    """
    Lists the quote, its author and date created fields for display in admin
    """
    list_display = ("quote", "author", "created_on")
    search_fields = ["quote", "author"]

    class Meta:
        ordering = ["-created_on"]


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """
    Lists the name and read fields for display in admin
    """
    list_display = ("name", "read",)

# Register your models here.
