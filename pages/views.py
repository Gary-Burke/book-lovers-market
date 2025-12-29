from django.shortcuts import render
from django.contrib import messages
from .models import Home
from .forms import FeedbackForm

# Create your views here.


def about_us(request):

    if request.method == "POST":
        feedback_form = FeedbackForm(data=request.POST)
        if feedback_form.is_valid():
            feedback_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Feedback submitted! Thank you for your input"
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                "Unable to submit feedback. Please try again later"
            )

    feedback_form = FeedbackForm()

    return render(
        request,
        "pages/about.html",
        {
            "feedback_form": feedback_form,
        }
    )


def home_page(request):

    home = Home.objects.all().order_by("-created_on").first()

    return render(
        request,
        "pages/home.html",
        {"home": home,
         }
    )
