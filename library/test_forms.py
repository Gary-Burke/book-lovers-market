from django.test import TestCase
from .forms import ISBNForm, EditBookForm

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


class TestEditBookForm(TestCase):

    def test_form_is_valid(self):
        """Test all field to be valid"""
        form = EditBookForm({
            "title": "Some Book",
            "author": "Some Author",
            "isbn": "123456789",
            "status": "0"
        })
        self.assertTrue(
            form.is_valid(),
            msg="Form is valid")

    def test_title_is_required(self):
        """Test 'title' field to be not empty"""
        form = EditBookForm({
            "title": "",
            "author": "Some Author",
            "isbn": "123456789",
            "status": "0"
        })
        self.assertFalse(
            form.is_valid(),
            msg="Title was not entered but form is valid")
    
    def test_author_is_required(self):
        """Test 'author' field to be not empty"""
        form = EditBookForm({
            "title": "Some Book",
            "author": "",
            "isbn": "123456789",
            "status": "0"
        })
        self.assertFalse(
            form.is_valid(),
            msg="Author was not entered but form is valid")
        
    def test_isbn_is_required(self):
        """Test 'isbn' field to be not empty"""
        form = EditBookForm({
            "title": "Some Book",
            "author": "Some Author",
            "isbn": "",
            "status": "0"
        })
        self.assertFalse(
            form.is_valid(),
            msg="ISBN was not entered but form is valid")
        
    def test_status_is_required(self):
        """Test 'status' field to be not empty"""
        form = EditBookForm({
            "title": "Some Book",
            "author": "Some Author",
            "isbn": "123456789",
            "status": ""
        })
        self.assertFalse(
            form.is_valid(),
            msg="Status was not entered but form is valid")
