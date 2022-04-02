from dataclasses import fields
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View # <- View class to handle requests
from django.http import HttpResponse, HttpResponseRedirect # <- a class to handle sending a type of response
from .models import Cookie
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


# Cookie Views
class Cookies(TemplateView):
    template_name='cookies.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')

        if name !=None:
            context["cookies"] = Cookie.objects.filter(name__icontains=name)
            context['header'] = f'searching for {name}'
        else:
            context['cookies'] = Cookie.objects.all()
            context['header'] = "Cookies"
        return context        







# Bakery Views
# Login, Logout, and SignUp

def login_view(request):
    # if post, then authenticate (user submitted username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password'] 
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    return render(request, 'login.html', {'form': form})
                    # feel free to redirect them somewhere
            else: 
                return render(request, 'signup.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})    