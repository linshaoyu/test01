from django.shortcuts import render
from django.http import HttpResponse
import logging
from .forms import AddForm

logging.basicConfig(level=logging.INFO)


# Create your views here.

def view(request):
    logging.info("views.view")
    return HttpResponse(u"hello world")


def index(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data["a"]
            b = form.cleaned_data["b"]
            return HttpResponse(str(int(a) + int(b)))
    else:
        form = AddForm()

    return render(request, "index.html", {"form": form})
