from dataclasses import fields
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View # <- View class to handle requests
from django.http import HttpResponse, HttpResponseRedirect # <- a class to handle sending a type of response
# from .models import 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'