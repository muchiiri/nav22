from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Quote, Quote_Air, Quote_Sea, Quote_Road, Quote_Warehouse, QuoteType

# Create your views here.
class QuoteTypeCreateView(CreateView):
    model = QuoteType
    fields = ['type', 'date']
    template_name = 'quote/type_form.html'
    success_url = '/create/'
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class QuoteCreateView(CreateView):
    model = Quote
    fields = ['incoterm','other_vas','county_origin','county_destination','cargo_description','goods_category','special_delivery']
    template_name = 'quote/create.html'
    success_url = '/quote/list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Quote'
        return context
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)