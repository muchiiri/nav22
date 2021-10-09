from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    
    
    
    # path('/editfreight/',editRoadFreigh, name='viewedit'),
    path('editfreight/',editRoadFreigh, name='viewedit'),
]
