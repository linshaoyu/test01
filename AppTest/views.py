import logging

from django.http import HttpResponse
from django.shortcuts import render

from .models import *
from django.views import generic

from .forms import AddForm

logging.basicConfig(level=logging.INFO)


# Create your views here.


class ResultsView(generic.ListView):
    model = GameInfo
    template_name = "list.html"

    def get_queryset(self):
        return GameInfo.objects.all()


class DetailView(generic.DetailView):
    model = GameInfo
    template_name = "form.html"


def view(request):
    logging.info("views.view")
    return render(request, "index.html")


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
