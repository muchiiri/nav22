from cProfile import label
from pyexpat import model
from django import forms
from .models import Quotation,Staff_Quotation,Admin_Quotation,Quotation_Type,Quotation_Air,Quotation_Sea,Quotation_Road,Quotation_Warehouse
from crispy_forms.helper import FormHelper

class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        exclude=('staff',)

        labels={
            'goods_category':'Are gooods categorized as dangerous'
        }

#Quotation Type
class QuotationTypeForm(forms.ModelForm):
    class Meta:
        model = Quotation_Type
        fields = ('type','owner',)
        labels={
            'type':'What type of quotation do you need?'
        }

#Quotation_Air form
class Quotation_Air(forms.ModelForm):
    class Meta:
        model = Quotation_Air
        fields = ('incoterms','other_vas','cargo_weight','cargo_length','cargo_width','cargo_height',
        'country_origin','collection_address','cargo_description','goods_category','special_instructions')

#staff pricing form
class StaffQuotationForm(forms.ModelForm):
    class Meta:
        model = Staff_Quotation
        fields = ('__all__')
        # exclude = ('quotation',)

class AdminQuotationForm(forms.ModelForm):
    class Meta:
        model = Admin_Quotation
        fields = ('__all__')

#client pricing form: view quote reply
class ClientQuotationPricing(forms.ModelForm):
    class Meta:
        model = Staff_Quotation
        exclude = ('buying_origin_haulage','margin_origin_haulage',
        'buying_customs_documentation','margin_customs_documentation',
        'buying_origin_terminal_handling','margin_origin_terminal_handling',
        'buying_port_charges','margin_port_charges',
        'buying_other_charges','margin_other_charges',
        'buying_freight_cost','margin_freight_cost',
        'buying_other_freight_charges','margin_other_freight_charges',
        'buying_total_origin','margin_total_origin',
        'buying_terminal_handling','margin_terminal_handling',
        'buying_port_charges_dest','margin_port_charges_dest',
        'buying_agency_fee','margin_agency_fee',
        'buying_transport_delivery','margin_transport_delivery',
        'buying_other_destination_charges','margin_other_destination_charges',
        'buying_total_destination','margin_total_destination',
        )

    def __init__(self, *args, **kwargs):
        super(ClientQuotationPricing, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False