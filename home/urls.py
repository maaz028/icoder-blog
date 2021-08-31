
from django.contrib import admin
from django.http import request
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about_us', views.about_us, name='about_us'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('search_data', include('blogapp.urls')),
    path('signup', views.handle_signup, name='signup'),
    path('login', views.handle_login, name='login'),
    path('logout', views.handle_logout, name='logout'),
]
