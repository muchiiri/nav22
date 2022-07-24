from django.shortcuts import render,HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from requests import request
from .models import Quote, Quote_Air, Quote_Sea, Quote_Road, Quote_Warehouse, QuoteType
from datetime import date
# Create your views here.
class QuoteTypeCreateView(CreateView):
    model = QuoteType
    fields = ['type', 'date']
    template_name = 'type_form.html'
    success_url = '/quotation/create/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        #get today date
        today = date.today()
        d1 = today.strftime("%Y-%m-%d")
        context['date'] = d1
        return context

    def form_valid(self, form):
        if form.cleaned_data['type'] == 'Air':
            self.request.session['type'] = 'quote:create_air'
            form.instance.owner = self.request.user
            super().form_valid(form)
            return HttpResponseRedirect('/quotation/air/create/')

        elif form.cleaned_data['type'] == 'Sea':
            self.request.session['type'] = 'quote:create_sea'
            form.instance.owner = self.request.user
            super().form_valid(form)
            return HttpResponseRedirect('/quotation/sea/create/')

        elif form.cleaned_data['type'] == 'Road':
            self.request.session['type'] = 'quote:create_road'
            form.instance.owner = self.request.user
            super().form_valid(form)
            return HttpResponseRedirect('/quotation/road/create/')

        elif form.cleaned_data['type'] == 'Warehouse':
            self.request.session['type'] = 'quote:create_warehouse'
            form.instance.owner = self.request.user
            super().form_valid(form)
            return HttpResponseRedirect('/quotation/warehouse/create/')
            
        # form.instance.owner = self.request.user
        # return super().form_valid(form)

#create sea quote
class QuoteCreateView_Sea(CreateView):
    model = Quote_Sea
    fields = ['incoterm','other_vas','county_origin','county_destination','cargo_description','goods_category','special_delivery']
    template_name = 'create.html'
    success_url = '/quotation/list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Quote'
        context['type'] = 'Sea'
        print(context['type'])
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

#create air quote
class QuoteCreateView_Air(CreateView):
    model = Quote_Air
    fields = ['incoterm','other_vas','county_origin','county_destination','cargo_description','goods_category','special_delivery','cargo_weight','cargo_dimension_length','cargo_dimension_width','cargo_dimension_height']
    template_name = 'create.html'
    success_url = '/quotation/list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Quote'
        context['type'] = 'Air'
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

#create road quote
class QuoteCreateView_Road(CreateView):
    model = Quote_Road
    fields = ['incoterm','other_vas','county_origin','county_destination','cargo_description','goods_category','special_delivery','cargo_weight','cargo_dimension_length','cargo_dimension_width','cargo_dimension_height']
    template_name = 'create.html'
    success_url = '/quotation/list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Quote'
        context['type'] = 'Road'
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

#create warehouse quote
class QuoteCreateView_Warehouse(CreateView):
    model = Quote_Warehouse
    fields = ['cargo_description','cargo_weight','cargo_dimension_length','cargo_dimension_width','cargo_dimension_height','special_delivery']
    template_name = 'create.html'
    success_url = '/quotation/list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Quote'
        context['type'] = 'Warehouse'
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

#list quotation
class QuoteListView(ListView):
    model = Quote
    
    def get_queryset(self):
        return Quote.objects.filter(owner=self.request.user)

    template_name = 'quote_list.html'


#detailed quotation
class QuoteDetailView(ListView):
    model = Quote
    template_name = 'quote_detail.html'

    def get_queryset(self):
        return Quote.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Quote Detail'
        return context

#edit quotation
class QuoteEditView(ListView):
    model = Quote
    template_name = 'quote_edit.html'

    def get_queryset(self):
        return Quote.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Quote Edit'
        return context