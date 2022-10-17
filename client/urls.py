from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('',home ,name='client_home'),
    #complete shipments index for clients
    path('index_complete/',homecomplete, name='indexcomplete'),
    # path('indexold', homecomplete, name='old'),
    path('view/<int:uid>/<str:refno>/',view ,name='view'),
    path('view2/<int:uid>/<str:refno>/',view2 ,name='view2'),
    path('view3/<int:uid>/<str:refno>/',view3 ,name='view3'),
]