from django.contrib import admin
from django.urls import path, include # new
from django.contrib.auth import views as auth_views

urlpatterns = [
    
     # new
    path('accounts/login', auth_views.login, name='login'),
    # accounts/login/ [name='login']
    # accounts/logout/ [name='logout']
    # path(accounts/password_change/ [name='password_change']),
    # accounts/password_change/done/ [name='password_change_done']
    # accounts/password_reset/ [name='password_reset']
    # accounts/password_reset/done/ [name='password_reset_done']
    # accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # accounts/reset/done/ [name='password_reset_complete']
]