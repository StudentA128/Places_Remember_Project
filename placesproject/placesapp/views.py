from django.shortcuts import render

from .forms import PlacesForm
from .models import Places


def index(request):
    if request.user.is_authenticated:

        user_name = request.user
        error = ""

        if request.method == "POST":
            form = PlacesForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                error = "Form is incorrect"

        places = Places.objects.filter(user_id=user_name)
        form = PlacesForm()
        context = {
            "form": form,
            "places": places,
            "error": error,
        }
        return render(request, "placesapp/home.html", context)
    else:
        return render(request, "placesapp/welcome.html")


def home(request):
    if request.user.is_authenticated:

        user_name = request.user
        error = ""

        if request.method == "POST":
            form = PlacesForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                error = "Form is incorrect"

        places = Places.objects.filter(user_id=user_name)
        form = PlacesForm()
        context = {
            "form": form,
            "places": places,
            "error": error,
        }
        return render(request, "placesapp/home.html", context)
    else:
        return render(request, "placesapp/welcome.html")
