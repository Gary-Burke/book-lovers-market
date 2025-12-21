import requests
from django.shortcuts import render, redirect
from .forms import ISBNForm
from .models import Book
from django.contrib import messages

# Create your views here.


def library_books(request):
    return render(
        request,
        "library/library.html",
    )


def fetch_book_by_isbn(isbn):
    """
    Fetches an object from Google Books API based on the ISBN argument.
    Returns the book title, author and thumbnail image of given ISBN.
    """
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
    """
    Displays a form to enter ISBN number
    Calls fetch_book_by_isbn view and passes user input as ISBN
    If the ISBN is found, then it will update the Book model
    """
    if request.method == "POST":
        add_form = ISBNForm(request.POST)

        if add_form.is_valid():
            isbn = add_form.cleaned_data["isbn"]
            book_data = fetch_book_by_isbn(isbn)

            if book_data:
                Book.objects.create(
                    user=request.user,
                    title=book_data["title"],
                    author=book_data["author"],
                    isbn=book_data["isbn"],
                    cover_url=book_data["cover_url"],
                )
                messages.add_message(
                    request, messages.SUCCESS,
                    "Book successfully added to your Library!"
                )

            else:
                messages.add_message(
                    request, messages.ERROR,
                    "Book not found!"
                )

    add_form = ISBNForm()

    return render(
        request,
        "library/add_book.html",
        {"add_form": add_form}
    )
