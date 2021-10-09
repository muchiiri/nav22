from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('',home ,name='fielduser_home'),
    path('index_completed/',home2 ,name='completed_shipments'),
    path('cargoroad',RoadFreightShip_view, name='road'),
    path('cargosea',SeaFreightShip_view, name='sea'),
    path('cargoair',AirFreightShip_view, name='air'),
    path('edit/<userid>/<str:refno>/',editRoadFreigh, name='roadedit'),
    path('edit2/<userid>/<str:refno>/',editSeaFreigh, name='seaedit'),
    path('edit3/<userid>/<str:refno>/',editAirFreigh, name='airedit'),
    path('view/<int:uid>/<str:refno>/',view ,name='view'),
    path('view2/<int:uid>/<str:refno>/',view2 ,name='view2'),
    path('view3/<int:uid>/<str:refno>/',view3 ,name='view3'),
    path('freightforward/',FreightForwardingView, name='edit'),
    path('staffcommentsform/',StaffFreightForwardingEdit, name='staffcomment'),
]
