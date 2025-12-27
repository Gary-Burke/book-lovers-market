from django.shortcuts import render

# Create your views here.


def about_us(request):
    return render(
        request,
        "pages/about.html",
    )


def home_page(request):
    return render(
        request,
        'pages/home.html'
    )
