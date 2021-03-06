from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'), #login page will be the first thing users see
    path('signup/', views.signup_view, name = 'signup'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.Home.as_view(), name="home"),
    path('user/<username>/', views.profile, name='profile'),
    path('cookies/', views.Cookies.as_view(), name ='cookies'),
    path('cookies/new', views.CreateCookie.as_view(), name ='create_cookie'),
    path('cookies/<int:pk>/', views.CookieDetail.as_view(), name = "cookie_detail"),
    path('cookie/<int:pk>/update', views.UpdateCookie.as_view(), name = "update_cookie"),
    path('cookie/<int:pk>/delete', views.DeleteCookie.as_view(), name = "delete_cookie"),

    path('bakeries/', views.bakeries, name='bakeries'),
    path('bakeries/<int:bakery_id>/', views.bakery_details, name='bakery_detail'),
    path('bakeries/create/', views.CreateBakery.as_view(), name='create_bakery'),
    path('bakeries/<int:pk>/update/', views.UpdateBakery.as_view(), name='update_bakery'),
    path('bakeries/<int:pk>/delete/', views.DeleteBakery.as_view(), name='delete_bakery'),
]