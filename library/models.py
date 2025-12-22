from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Owned"), (1, "For Sale"), (2, "Sold"))

# Create your models here.


class Book(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="books"
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=30)
    cover_url = models.URLField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    price = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-title"]

    def __str__(self):
        return f"Title: {self.title} | Author({self.author})"
