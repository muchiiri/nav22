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
    path('client_approval/',clientApproval,name="client_approval"),

    path('edit/<int:pk>/',QuoteEditView.as_view(),name="edit"),
    path('detail/<str:quote_serial>/<str:quote_type>/<int:pk>/<str:incoterm>/',detailed_quote,name="detail"),
    
    #path('pendingQuotes/<str:quote_serial>/<str:quote_type>/<int:pk>/<str:incoterm>/',pendingQuotes,name="pending_quotes"),
    
    #staff urls
    path('staff/list/',StaffQuoteListView.as_view(),name="staff_list"),
    path('staff/pricing/',staff_Add_Pricing,name="staff_add_pricing"),
    path('staff/view_pricing/',view_Staff_Pricing_List,name="staff_view_pricing"),
    path('staff/view_pricing/<int:pk>/',view_Staff_Pricing_Detailed,name="staff_detailed_pricing"),
    path('staff/approval',adminApproval,name="admin_approval"),

    #download urls
    path('download/<str:quote_app>/',download_pdf_pricing,name="download_pricing"),
]
