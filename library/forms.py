from django import forms
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
