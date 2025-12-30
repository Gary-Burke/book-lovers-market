from django.urls import path
from . import views
from .views import BookDetailView


urlpatterns = [
    path('', views.BookList.as_view(), name='library'),
    path('add/', views.add_book_by_isbn, name='add_book'),
    path('add_manual/', views.add_book_manual, name='add_book_manual'),
    path('delete_book/<int:book_id>', views.delete_book, name='delete_book'),
    path('edit_book/<int:book_id>', views.edit_book, name='edit_book'),
    path('sales/', views.SalesList.as_view(), name='sales'),
    path('sales/book_details/<int:pk>/',
         BookDetailView.as_view(),
         name='book_details'),
]
