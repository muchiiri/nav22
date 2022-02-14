from django.contrib import admin
from django.urls import path,include
from .views import *
app_name = "reports"
urlpatterns = [
    
    #client
    path('',report ,name='report'),
    path('download_sea_report',report_download_sea,name="report_sea"),
    path('download_road_report',report_download_road,name="report_road"),
    path('download_air_report',report_download_air,name="report_air"),
    path('summary_report',report_summary_charts,name="report_summary"),

    #fielduser
    path('fielduser_report',fielduser_report,name="fielduser_report"),
]