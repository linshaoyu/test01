import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .forms import *
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
    template_name = "form.html"

    # def get_object(self, queryset=None):
    #     pk = self.kwargs.get(self.pk_url_kwarg)
    #     gameInfo = GameInfo.objects.get(pk=pk)
    #     print(gameInfo)
    #     form = GameInfoForm(instance=gameInfo)
    #     return form


def detail(request, pk):
    logging.info("detail")
    if request.method == "POST":
        logging.info("post")
    else:
        logging.info("get:" + pk)
        if not pk.strip():
            form = GameInfoForm
        else:
            gameinfo = GameInfo.objects.get(pk=pk)
            form = GameInfoForm(instance=gameinfo)
    return render(request, "form.html", {"form": form})


def save(request):
    if request.method == "POST":
        form = GameInfoForm(request.POST)
        if form.is_valid():
            new_gameinfo = form.save()
            print(new_gameinfo)
    else:
        form = GameInfoForm
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
