import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import *

from .forms import AddForm

logging.basicConfig(level=logging.INFO)


# Create your views here.

def view(request):
    logging.info("views.view")
    return render(request, "index.html")


def DetailView():
    model = GameInfo
    template_name = "form.html"


def ResultsView():
    model = GameInfo
    template_name = "list.html"


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
