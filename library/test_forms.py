from django.test import TestCase
from .forms import ISBNForm

# Create your tests here.


class TestISBNForm(TestCase):

    def test_form_is_valid(self):
        """Test 'isbn' field to be valid"""
        form = ISBNForm({
            "isbn": ""
        })
        self.assertFalse(
            form.is_valid(),
            msg="ISBN must be entered")
