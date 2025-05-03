from django.shortcuts import render


# Create your views here.
def hello(request):
    greetings = {
        "greetings": "Assalam-O-Alaikum World From Django."
    }
    return render(request, "start/index.html", greetings)
