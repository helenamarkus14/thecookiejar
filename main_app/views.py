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

#Create new cookie
@method_decorator(login_required, name='dispatch')
class Create_Cookie(CreateView):
    model = Cookie
    fields = '__all__'
    template_name = 'create_cookie.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/cookies')
class Cookie_Detail(DetailView):  
    model = Cookie
    template_name = 'cookie_detail.html'      

# Update Cookie
@method_decorator(login_required, name='dispatch') 
class Update_Cookie(UpdateView):
    model = Cookie
    fields ='__all__'
    template_name = 'update_cookie.html'
    def get_success_url(self):
        return reverse('cookie_detail', kwargs={'pk': self.object.pk})

# Delete Cookie
@method_decorator(login_required, name='dispatch') 
class Delete_Cookie(DeleteView):
    model = Cookie
    template_name = 'delete_cookie.html'
    success_url = '/cookies/'


# Bakery Views






# profile

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    cookies = Cookie.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'cookies': cookies}) 
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

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('Hi', user.username)
            return HttpResponseRedirect('/user/'+str(user))
        else:
            return render(request, 'signup.html', {'form': form})   
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
        
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')        