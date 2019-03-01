from django.contrib import admin
from django.urls import path
from . import views 
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import *

urlpatterns = [
    path('new/', views.new, name='new'),
    path('create', views.create, name="create"),
    path('', views.portfolio, name="portfolio"),
]