from . import views
from django.urls import path

urlpatterns = [
    path('about/', views.about_us, name='about'),
    path('sales/', views.sales_page, name='sales'),
    path('', views.home_page, name='home'),
]
