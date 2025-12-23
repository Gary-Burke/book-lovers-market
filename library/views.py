import requests
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import ISBNForm, EditBookForm
from .models import Book
from django.contrib import messages

# Create your views here.


class BookList(LoginRequiredMixin, generic.ListView):
    model = Book
    template_name = "library/library.html"

    def get_queryset(self):
        return Book.objects.filter(
            user=self.request.user
        ).order_by("author")


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
    Prevents duplicate ISBN to be added to user library
    """
    if request.method == "POST":
        add_form = ISBNForm(data=request.POST)

        if add_form.is_valid():
            isbn = add_form.cleaned_data["isbn"]
            book_data = fetch_book_by_isbn(isbn)

            if book_data:
                if Book.objects.filter(user=request.user, isbn=isbn).exists():
                    messages.add_message(
                        request, messages.WARNING,
                        "You have already added this book."
                    )
                else:
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


def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if book.user == request.user:
        book.delete()
        messages.add_message(
            request, messages.SUCCESS, "Book deleted!"
        )
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own books!"
        )
    return HttpResponseRedirect(reverse('library'))


def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == "POST":

        edit_book_form = EditBookForm(data=request.POST, instance=book)

        if edit_book_form.is_valid() and book.user == request.user:
            book = edit_book_form.save()
            messages.add_message(
                request, messages.SUCCESS, "Book details successfully updated!"
            )
        else:
            messages.add_message(
                request, messages.ERROR, "Unable to update book details!"
            )

        return HttpResponseRedirect(reverse('library'))

    else:
        edit_book_form = EditBookForm(instance=book)

    return render(
        request,
        "library/edit_book.html",
        {
            "book": book,
            "edit_book_form": edit_book_form,
        }
    )
