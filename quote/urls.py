from django.urls import path,include
from .views import *
app_name = "quote"
urlpatterns = [
    path('type/', QuoteTypeCreateView.as_view(), name='type'),
    path('create/',QuoteCreateView.as_view(),name="create"),
]
