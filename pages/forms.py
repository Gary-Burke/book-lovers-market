from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    """
    Form class for users to provide feedback
    """
    class Meta:
        """
        Django model: Feedback
        Fields to add to form
        """
        model = Feedback
        fields = (
            "name", "email", "feedback"
        )
