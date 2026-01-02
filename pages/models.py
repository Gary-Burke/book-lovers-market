from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Home(models.Model):
    """
    Stores a single instance for the home page content
    """
    image = CloudinaryField('image', default='placeholder')
    quote = models.TextField()
    author = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} | {self.quote}"


class Feedback(models.Model):
    """
    Stores a single feedback message from a user
    """
    name = models.CharField(max_length=255)
    email = models.EmailField()
    feedback = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Feedback from {self.name}"
