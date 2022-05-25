from cProfile import label
from pyexpat import model
from django import forms
from .models import Quotation,Staff_Quotation,Admin_Quotation

class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        exclude=('staff',)

        labels={
            'goods_category':'Are gooods categorized as dangerous'
        }

class StaffQuotationForm(forms.ModelForm):
    class Meta:
        model = Staff_Quotation
        fields = ('__all__')
        # exclude = ('quotation',)

class AdminQuotationForm(forms.ModelForm):
    class Meta:
        model = Admin_Quotation
        fields = ('__all__')