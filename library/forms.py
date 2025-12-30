from django import forms
from .models import Book
import re


class ISBNForm(forms.Form):
    isbn = forms.CharField(
        max_length=30,
        label="ISBN",
        widget=forms.TextInput(attrs={"placeholder": "Enter ISBN"})
    )

    def clean_isbn(self):
        isbn = self.cleaned_data["isbn"]
        return re.sub(r"[-\s]", "", isbn)


class EditBookForm(forms.ModelForm):
    """
    Form class for users to edit their book details
    """
    class Meta:
        """
        Django model: Book
        Fields to add to form model
        """
        model = Book
        fields = (
            "title", "author", "isbn", "cover_url",
            "status", "price", "comments",
        )
