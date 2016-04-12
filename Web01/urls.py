"""Web01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from AppTest import views

urlpatterns = [
   # url(r"^$", views.index),
    url(r"^index$", views.ResultsView.as_view()),
    url(r"^detail/(?P<pk>[a-zA-Z]+)/$", views.DetailView.as_view(), name="detail"),
    url(r"^hello$", views.view),
   # url(r"^detail$", views.DetailView.as_view),
    url(r'^admin/', admin.site.urls),
]
