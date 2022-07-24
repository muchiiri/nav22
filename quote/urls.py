from django.urls import path,include
from .views import *
app_name = "quote"
urlpatterns = [
    path('type/', QuoteTypeCreateView.as_view(), name='type'),
    path('sea/create/',QuoteCreateView_Sea.as_view(),name="create_sea"),
    path('air/create/',QuoteCreateView_Air.as_view(),name="create_air"),
    path('road/create/',QuoteCreateView_Road.as_view(),name="create_road"),
    path('warehouse/create/',QuoteCreateView_Warehouse.as_view(),name="create_warehouse"),
    path('list/',QuoteListView.as_view(),name="list"),

    path('edit/<int:pk>/',QuoteEditView.as_view(),name="edit"),
    # path('delete/<int:pk>/',QuoteDeleteView.as_view(),name="delete"),
]
