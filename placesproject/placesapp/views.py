from django.shortcuts import render

from .forms import PlacesForm


def index(request):
    if request.user.is_authenticated:
        error = ""
        if request.method == "POST":
            form = PlacesForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                error = "Form is incorrect"

        form = PlacesForm()
        context = {
            "form": form,
            "error": error,
        }
        return render(request, "placesapp/home.html", context)
    else:
        return render(request, "placesapp/welcome.html")


def home(request):
    if request.user.is_authenticated:
        error = ""
        if request.method == "POST":
            form = PlacesForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                error = "Form is incorrect"

        form = PlacesForm()
        context = {
            "form": form,
            "error": error,
        }
        return render(request, "placesapp/home.html", context)
    else:
        return render(request, "placesapp/welcome.html")
