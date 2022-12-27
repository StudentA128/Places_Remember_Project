from django.shortcuts import render


def index(request):
    if request.user.is_authenticated:
        return render(request, "placesapp/home.html")
    else:
        return render(request, "placesapp/welcome.html")


def home(request):
    if request.user.is_authenticated:
        return render(request, "placesapp/home.html")
    else:
        return render(request, "placesapp/welcome.html")
