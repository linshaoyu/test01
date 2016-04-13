import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .forms import AddForm
from .models import *

logging.basicConfig(level=logging.INFO)


# Create your views here.


class ResultsView(generic.ListView):
    model = GameInfo
    template_name = "list.html"

    def get_queryset(self):
        return GameInfo.objects.all()


class DetailView(generic.DetailView):
    logging.info("===DetailView====")
    model = GameInfo
    model = GameInfoForm(model)
    template_name = "form.html"


"""
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        return context
"""


def detail(request, gameCode):
    logging.info("detail")
    if (request.method == "POST"):
        logging.info("post")
    else:
        logging.info("get")
        gameInfo = GameInfo.objects.get(pk=gameCode)
        form = GameInfoForm(instance=gameInfo)
    return render(request, "form.html", {"form": form})


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
