from django.contrib import admin
from django.urls import path,include
from .views import *
app_name = "reports"
urlpatterns = [
    
    path('',report ,name='report'),
    path('download_sea_report',report_download_sea,name="report_sea"),
    path('download_road_report',report_download_road,name="report_road"),
    path('download_air_report',report_download_air,name="report_air"),
    path('download_temp',report_template,name="report_template"),
]