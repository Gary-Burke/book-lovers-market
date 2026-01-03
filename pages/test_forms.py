from django.test import TestCase
from .forms import FeedbackForm

# Create your tests here.


class TestFeedbackForm(TestCase):

    def test_form_is_valid(self):
        """Test all fields to be valid"""
        form = FeedbackForm({
            "name": "Guy",
            "email": "guy@xmail.com",
            "feedback": "I have something to say"
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_name_is_required(self):
        """Test to ensure 'name' field is not empty"""
        form = FeedbackForm({
            "name": "",
            "email": "guy@xmail.com",
            "feedback": "I have something to say"
        })
        self.assertFalse(
            form.is_valid(),
            msg="Name was not entered but the form is valid"
        )

    def test_email_is_required(self):
        """Test to ensure 'email' field is not empty"""
        form = FeedbackForm({
            "name": "Guy",
            "email": "",
            "feedback": "I have something to say"
        })
        self.assertFalse(
            form.is_valid(),
            msg="Email was not entered but the form is valid"
        )

    def test_feedback_is_required(self):
        """Test to ensure 'feedback' field is not empty"""
        form = FeedbackForm({
            "name": "Guy",
            "email": "guy@xmail.com",
            "feedback": ""
        })
        self.assertFalse(
            form.is_valid(),
            msg="Feedback was not entered but the form is valid"
        )
