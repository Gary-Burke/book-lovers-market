from django.contrib import admin
from .models import Home


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    """
    Lists message and read fields for display in admin
    """
    list_display = ("quote", "author", "created_on")
    search_fields = ["quote", "author"]

    class Meta:
        ordering = ["-created_on"]

# Register your models here.
