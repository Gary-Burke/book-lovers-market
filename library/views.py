import requests
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.db.models import Q
from .forms import ISBNForm, EditBookForm, ManualBookForm
from .models import Book

# Create your views here.


class BookList(LoginRequiredMixin, ListView):
    """
    Returns all books in :model:`library.Book`

    **Context**

    ``queryset``
    All instances of books in :model:`library.Book` that are
    related to :model:`auth.User`.
    queryset further filtered by:
     - Search input from user
     - Filter options based on field "status"
     - Ordered by user choice

     **Template:**

     :template:`library/library.html`
    """
    model = Book
    template_name = "library/library.html"
    paginate_by = 24

    def get_queryset(self):
        queryset = Book.objects.filter(user=self.request.user)

        # Filter by user input from search bar
        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(author__icontains=search) |
                Q(isbn__icontains=search)
            )

        # Filter by status selected by user
        status = self.request.GET.get("status")
        if status:
            queryset = queryset.filter(status=status)

        # Set order by based on user selection
        sort = self.request.GET.get("sort", "author")

        allowed_sorts = [
            "author", "-author",
            "title", "-title",
            "status", "-status",
        ]

        if sort not in allowed_sorts:
            sort = "author"

        return queryset.order_by(sort)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["STATUS"] = Book.STATUS
        context["current_sort"] = self.request.GET.get("sort", "author")
        return context


# Code from ChatGTP to help with Google Books API
def fetch_book_by_isbn(isbn):
    """
    Fetches an object from Google Books API based on the ISBN argument.
    Returns the book title, author, ISBN and thumbnail image url of given ISBN.
    """
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)
    data = response.json()

    if "items" not in data:
        return None

    volume = data["items"][0]["volumeInfo"]
    image_links = volume.get("imageLinks", {})

    thumbnail = image_links.get("thumbnail")
    if thumbnail:
        thumbnail = thumbnail.replace("http://", "https://", 1)

    return {
        "title": volume.get("title", "Unknown Title"),
        "author": ", ".join(volume.get("authors", ["Unknown Author"])),
        "isbn": isbn,
        "cover_url": thumbnail,
    }


def add_book_by_isbn(request):
    """
    Creates an instance of :model:`library.Book`
    Calls fetch_book_by_isbn view and passes user input as ISBN

    **Context**

    ``add_form``
        An instance of :form:`library.ISBNForm`
    ``book_data``
        Data obtained from Google Books API used to create
        an instance of :model:`library.Book`
    ``active``
        Argument passed to template to determine class assignment

    **Template**

    :template:`library/add_book.html`
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
        {
            "add_form": add_form,
            "active": "isbn"
        }
    )


def add_book_manual(request):
    """
    Creates an instance of :model:`library.Book`

    **Context**

    ``add_form_manual``
        An instance of :form:`library.ManualBookForm`
    ``active``
        Argument passed to template to determine class assignment

    **Template**

    :template:`library/add_book.html`
    """
    if request.method == "POST":
        add_form_manual = ManualBookForm(data=request.POST)

        if add_form_manual.is_valid():
            isbn = add_form_manual.cleaned_data["isbn"]
            title = add_form_manual.cleaned_data["title"]
            if Book.objects.filter(
                    user=request.user, isbn=isbn).exists():
                messages.add_message(
                    request, messages.WARNING,
                    "You have already added this ISBN."
                )
            elif Book.objects.filter(
                    user=request.user, title=title).exists():
                messages.add_message(
                    request, messages.WARNING,
                    "You have already added this title."
                )
            else:
                book = add_form_manual.save(commit=False)
                book.user = request.user
                book.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    "Book successfully added to your Library!"
                )
        else:
            messages.add_message(
                request, messages.ERROR,
                "Unable to add book. Please try again later"
            )

    add_form_manual = ManualBookForm()

    return render(
        request,
        "library/add_book.html",
        {
            "add_form_manual": add_form_manual,
            "active": "manual"
        },
    )


def delete_book(request, book_id):
    """
    Delete an individual book entry.

    **Context**

    ``book``
        An instance of :model:`library.Book`.
    """
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
    """
    Display an individual book to be edited.

    **Context**

    ``book``
        An instance of :model:`library.Book`.
    ``edit_book_form``
        An instance of :form:`library.EditBookForm`

    **Template**

    :template:`library/edit_book.html`
    """
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


class SalesList(ListView):
    """
    Returns all books in :model:`library.Book`

    **Context**

    ``queryset``
    All instances of books in :model:`library.Book` that are for sale.

    queryset further filtered by:
     - Search input from user
     - Ordered by user choice

     **Template:**

     :template:`library/sales.html`
    """
    model = Book
    template_name = "library/sales.html"
    context_object_name = "sales_list"
    paginate_by = 24

    def get_queryset(self):
        queryset = Book.objects.filter(status=1)

        # Filter by user input from search bar
        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(author__icontains=search) |
                Q(isbn__icontains=search)
            )

        # Set order by based on user selection
        sort = self.request.GET.get("sort")

        allowed_sorts = [
            "author", "-author",
            "title", "-title",
            "price", "-price",
        ]

        if sort not in allowed_sorts:
            sort = "author"

        return queryset.order_by(sort)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_sort"] = self.request.GET.get("sort", "author")
        return context


class BookDetailView (DetailView):
    """
    Renders an individual book from :model:`library.Book`.

    **Context**

    ``book``
        An instance of :model:`library.Book`.

    **Template:**

    :template:`library/book_details.html`
    """
    model = Book
    template_name = "library/book_details.html"
    context_object_name = "book"
