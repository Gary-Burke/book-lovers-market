from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Home(models.Model):
    image = CloudinaryField('image', default='placeholder')
    quote = models.TextField()
    author = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} | {self.quote}"
