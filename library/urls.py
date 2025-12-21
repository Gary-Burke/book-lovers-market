from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookList.as_view(), name='library'),
    path('add/', views.add_book_by_isbn, name='add_book'),
]
