import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ISBNForm
from .models import Book
from django.http import HttpResponse

# Create your views here.


@login_required
def library_books(request):
    return HttpResponse("Hello, World!")


def fetch_book_by_isbn(isbn):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)
    data = response.json()

    if "items" not in data:
        return None

    volume = data["items"][0]["volumeInfo"]

    return {
        "title": volume.get("title", "Unknown Title"),
        "author": ", ".join(volume.get("authors", ["Unknown Author"])),
        "isbn": isbn,
    }


@login_required
def add_book_by_isbn(request):
    if request.method == "POST":
        form = ISBNForm(request.POST)
        if form.is_valid():
            isbn = form.cleaned_data["isbn"]
            book_data = fetch_book_by_isbn(isbn)

            if book_data:
                Book.objects.create(
                    user=request.user,
                    title=book_data["title"],
                    author=book_data["author"],
                    isbn=book_data["isbn"],
                )
                return redirect("library")
            else:
                form.add_error("isbn", "Book not found.")

    else:
        form = ISBNForm()

    return render(
        request,
        "library/add_book.html",
        {"form": form}
    )
