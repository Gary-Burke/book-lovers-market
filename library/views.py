import requests
from django.shortcuts import render, redirect
from .forms import ISBNForm
from .models import Book
from django.http import HttpResponse

# Create your views here.


def library_books(request):
    return HttpResponse("Hello, World!")


def fetch_book_by_isbn(isbn):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)
    data = response.json()

    if "items" not in data:
        return None

    volume = data["items"][0]["volumeInfo"]
    image_links = volume.get("imageLinks", {})

    return {
        "title": volume.get("title", "Unknown Title"),
        "author": ", ".join(volume.get("authors", ["Unknown Author"])),
        "isbn": isbn,
        "cover_url": image_links.get("thumbnail"),
    }


def add_book_by_isbn(request):
    if request.method == "POST":
        form_add = ISBNForm(request.POST)
        if form_add.is_valid():
            isbn = form_add.cleaned_data["isbn"]
            book_data = fetch_book_by_isbn(isbn)

            if book_data:
                Book.objects.create(
                    user=request.user,
                    title=book_data["title"],
                    author=book_data["author"],
                    isbn=book_data["isbn"],
                    cover_url=book_data["cover_url"],
                )
                return redirect("library")
            else:
                form_add.add_error("isbn", "Book not found.")

    else:
        form_add = ISBNForm()

    return render(
        request,
        "library/add_book.html",
        {"form_add": form_add}
    )
