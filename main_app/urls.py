from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.Home.as_view(), name="home"),
    path('cookies/', views.Cookies.as_view(), name='cookies')
]