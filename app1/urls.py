from os import name
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns= [

    path('register',views.register,name = 'register'),
    path('',views.login,name ="login"),
    path('profile/',views.profile, name = 'profile'),
    path('logout/',views.logout,name="logout")
   
]