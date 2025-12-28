from django.shortcuts import render
from .models import Home

# Create your views here.


def about_us(request):
    return render(
        request,
        "pages/about.html",
    )


def home_page(request):

    home = Home.objects.all().order_by("-created_on").first()

    return render(
        request,
        "pages/home.html",
        {"home": home,
         }
    )
