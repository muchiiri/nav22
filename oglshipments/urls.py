"""oglshipments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from dashboard import views
# from .views import indexHome,profileView
from .views import Home, handler404, profileView

urlpatterns = [
    # path("",indexHome),
    path("",Home),
    path("profile/",profileView),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('client/', include('client.urls')),
    path('keyuser/', include('keyuser.urls')),
    path('fielduser/', include('fielduser.urls')),
    path('shipments/', include('shipments.urls')),
    path('reports/', include('reports.urls')),
    path('quotation/',include('quote.urls')),
    path('quote/',include('quote.urls')),
    # path('dashboard/',include('dashboard.urls')),
    path('dashboard/', views.HomeView.as_view(), name= 'dashboard'),
    path('api', views.ChartData.as_view()),

    # Debug tool-bar
    path('__debug__/', include('debug_toolbar.urls')),
]

handler404 = 'oglshipments.views.handler404'
