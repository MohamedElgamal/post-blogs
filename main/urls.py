from django.contrib import admin
from django.urls import path, include
from .views import *
from main.views import *

urlpatterns = [
    path("", home, name="home_page"),
    path("", include("django.contrib.auth.urls")),
]
