from django.urls import path,include
from .views import *
from quote.views import *

app_name = "quote"

urlpatterns = [
    #client urls
    path('type/', QuoteTypeCreateView.as_view(), name='type'),
    path('sea/create/',QuoteCreateView_Sea.as_view(),name="create_sea"),
    path('air/create/',QuoteCreateView_Air.as_view(),name="create_air"),
    path('road/create/',QuoteCreateView_Road.as_view(),name="create_road"),
    path('warehouse/create/',QuoteCreateView_Warehouse.as_view(),name="create_warehouse"),
    path('list/',QuoteListView.as_view(),name="list"),

    path('edit/<int:pk>/',QuoteEditView.as_view(),name="edit"),
    path('detail/<str:quote_serial>/<str:quote_type>/',detailed_quote,name="detail"),
    # path('delete/<int:pk>/',QuoteDeleteView.as_view(),name="delete"),

    #staff urls
    path('staff/list/',StaffQuoteListView.as_view(),name="staff_list"),
]
