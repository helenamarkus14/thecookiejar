from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'), #login page will be the first thing users see
    path('signup/', views.signup_view, name = 'signup'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.Home.as_view(), name="home"),
    path('user/<username>/', views.profile, name='profile'),
    path('cookies/', views.Cookies.as_view(), name ='cookies'),
    path('cookies/new', views.Create_Cookie.as_view(), name ='create_cookie'),
    path('cookies/<int:pk>/', views.Cookie_Detail.as_view(), name = "cookie_detail"),
    path('cookie/<int:pk>/update', views.Update_Cookie.as_view(), name = "update_cookie"),
    path('cookie/<int:pk>/delete', views.Delete_Cookie.as_view(), name = "delete_cookie"),
]