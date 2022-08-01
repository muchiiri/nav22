from django.shortcuts import render,HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from requests import request
from .models import Quote, Quote_Air, Quote_App, Quote_Sea, Quote_Road, Quote_Warehouse, QuoteType
from datetime import date
# import heartrate
from birdseye import eye
# heartrate.trace(browser=True)
# Create your views here.

#generate a random serial number
@eye
def random_serial_no():
    import random
    import string
    serial_no = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    return serial_no

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

    # @eye
    def form_valid(self, form):
        if form.cleaned_data['type'] == 'Air':
            self.request.session['type'] = 'quote:create_air'
            self.request.session['type_name'] = 'Air'
            form.instance.owner = self.request.user
            form.instance.type = 'Quote_Air'
            # super().form_valid(form)
            return HttpResponseRedirect('/quotation/air/create/')

        elif form.cleaned_data['type'] == 'Sea':
            self.request.session['type'] = 'quote:create_sea'
            self.request.session['type_name'] = 'Sea'
            form.instance.owner = self.request.user
            form.instance.type = 'Quote_Sea'
            # super().form_valid(form)
            return HttpResponseRedirect('/quotation/sea/create/')

        elif form.cleaned_data['type'] == 'Road':
            self.request.session['type'] = 'quote:create_road'
            self.request.session['type_name'] = 'Road'
            form.instance.owner = self.request.user
            form.instance.type = 'Quote_Road'
            # super().form_valid(form)
            return HttpResponseRedirect('/quotation/road/create/')

        elif form.cleaned_data['type'] == 'Warehouse':
            self.request.session['type'] = 'quote:create_warehouse'
            self.request.session['type_name'] = 'Warehouse'
            form.instance.owner = self.request.user
            form.instance.type = 'Quote_Warehouse'
            # super().form_valid(form)
            return HttpResponseRedirect('/quotation/warehouse/create/')
            
        # form.instance.owner = self.request.user
        # return super().form_valid(form)

#create sea quote
class QuoteCreateView_Sea(CreateView):
    model = Quote_Sea
    fields = ['incoterm','other_vas','county_origin','county_destination','cargo_description','container_size','container_dimension_length','container_dimension_width','container_dimension_height','goods_category','special_delivery']
    template_name = 'create.html'
    success_url = '/quotation/list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Quote'
        context['type'] = 'Sea'
        print(context['type'])
        return context
    

    # @eye
    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.quote_serial_no = random_serial_no()
        form.instance.quote_type = self.request.session['type_name']
        return super().form_valid(form)

#create air quote
class QuoteCreateView_Air(CreateView):
    model = Quote_Air
    fields = ['incoterm','other_vas','county_origin','county_destination','collection_address','cargo_description','goods_category','special_delivery','cargo_weight','cargo_dimension_length','cargo_dimension_width','cargo_dimension_height']
    template_name = 'create.html'
    success_url = '/quotation/list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Quote'
        context['type'] = 'Air'
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.quote_serial_no = random_serial_no()
        form.instance.quote_type = self.request.session['type_name']
        return super().form_valid(form)

#create road quote
class QuoteCreateView_Road(CreateView):
    model = Quote_Road
    fields = ['truck_type','cargo_weight','cargo_dimension_length','cargo_dimension_width','cargo_dimension_height','collection_address','delivery_address']
    template_name = 'create.html'
    success_url = '/quotation/list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Quote'
        context['type'] = 'Road'
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.quote_serial_no = random_serial_no()
        form.instance.quote_type = self.request.session['type_name']
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
        form.instance.quote_serial_no = random_serial_no()
        form.instance.quote_type = self.request.session['type_name']
        return super().form_valid(form)

#list quotation
class QuoteListView(ListView):
    model = Quote_App
    
    @eye
    def get_queryset(self):
        return Quote_App.objects.filter(owner=self.request.user)

    @eye
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List Quotation'
        # context['quote_warehouse'] = Quote_Warehouse.objects.filter(owner=self.request.user)
        return context

    template_name = 'quote_list.html'


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

#detailed quotation
@eye
def detailed_quote(request, quote_serial,quote_type):
    if quote_type == 'Sea':
        quote = Quote.objects.get(quote_serial_no=quote_serial)
        quote_sea_detail = Quote_Sea.objects.get(quote_serial_no=quote_serial)
        return render(request, 'quote_detailed_sea.html', {'quote':quote,'quote_detail':quote_sea_detail})

    elif quote_type == 'Air':
        quote = Quote.objects.get(quote_serial_no=quote_serial)
        quote_air_detail = Quote_Air.objects.get(quote_serial_no=quote_serial)
        return render(request, 'quote_detailed_air.html', {'quote':quote,'quote_detail':quote_air_detail})

    elif quote_type == 'Road':
        quote = Quote.objects.get(quote_serial_no=quote_serial)
        quote_road_detail = Quote_Road.objects.get(quote_serial_no=quote_serial)
        return render(request, 'quote_detailed_road.html', {'quote':quote,'quote_detail':quote_road_detail})

    elif quote_type == 'Warehouse':
        # quote = Quote.objects.get(quote_serial_no=quote_serial)
        quote_warehouse_detail = Quote_Warehouse.objects.get(quote_serial_no=quote_serial)
        return render(request, 'quote_detailed_warehouse.html', {'quote_detail':quote_warehouse_detail})


#staff quote list
class StaffQuoteListView(ListView):
    model = Quote_App
    template_name = 'quote_list_staff.html'

    def get_queryset(self):
        return Quote_App.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List Quotation'
        return context