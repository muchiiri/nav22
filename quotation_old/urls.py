from django.contrib import admin
from django.urls import path
from .views import *
from quotation.quotationwizard import QuotationWizard
from quotation.forms import QuotationForm

app_name = 'quotation'

# FORMS = [("air_form", QuotationForm),]

urlpatterns = [
    #client url
    path('',quote_type ,name='quote_type'),
    path('air_form/',quote_air,name='air_form'),
    path('list',quote_list,name='quote_list'),
    path('detailed/<int:id>/',quote_detailed,name='quote_detail'),
    path('client_pricing/<int:quote_id>/<str:quote_incoterms>/',quote_pricing,name='quote_pricing'),
    path('client_approval/',client_decision,name='client_decision'),
    
    #staff url
    path('staff_list',staff_quote_list,name='staff_quote_list'),
    path('listall',staff_quote_list_all,name='staff_quote_list_all'),
    path('staff_detailed/<int:id>/',staff_quote_detailed,name='staff_quote_detail'),
    path('staff_pricing_approval/',admin_review,name='admin_review'),

    
    #wizard form
    #path('quotation_wizard/',QuotationWizard.as_view(),name='quotation_wizard'),
    
]
