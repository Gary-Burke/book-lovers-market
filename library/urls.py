from django.urls import path
from . import views


urlpatterns = [
    path('', views.library_books, name='library'),
]
