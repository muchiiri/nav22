from django.contrib import admin
from django.urls import path, include # new
from django.contrib.auth import views as auth_views

urlpatterns = [
    
     # new
    path('accounts/login', auth_views.login, name='login'),
]