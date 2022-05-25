from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'quotation'

urlpatterns = [
    #client url
    path('',quote_home ,name='quote_home'),
    path('list',quote_list,name='quote_list'),
    path('detailed/<int:id>/',quote_detailed,name='quote_detail'),
    
    #staff url
    path('staff_list',staff_quote_list,name='staff_quote_list'),
    path('staff_detailed/<int:id>/',staff_quote_detailed,name='staff_quote_detail'),

]
