from django.shortcuts import render
from django.http import HttpResponse
import logging

logging.basicConfig(level=logging.INFO)


# Create your views here.

def view(request):
    logging.info("views.view")
    return HttpResponse(u"hello world")
