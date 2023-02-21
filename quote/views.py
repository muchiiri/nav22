# from multiprocessing import popen_spawn_posix
from http.client import HTTPResponse
from venv import create
from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from requests import request
from .models import Quote, Quote_Air, Quote_App, Quote_Sea, Quote_Road, Quote_Warehouse, QuoteType, Staff_Pricing_Quotation,Taxes
from .models import Account
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import pdfkit
import os
from django.template.loader import render_to_string
import snoop
# import heartrate
from birdseye import eye
# from loguru import logger 
# heartrate.trace(browser=True)
# Create your views here.

#generate a random serial number
def random_serial_no():
    import random
    import string
    serial_no = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    return serial_no

# Client Select Quote Type
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

# Staff Select Quote Type
class QuoteTypeCreateViewStaff(CreateView):
    model = QuoteType
    fields = ['type', 'date', 'owner']
    template_name = 'type_form_staff.html'
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
            self.request.session['type_name'] = 'Air'
            self.request.session['owner'] = form.cleaned_data['owner'].id
            # form.instance.owner = self.request.session['owner']
            form.instance.type = 'Quote_Air'
            # super().form_valid(form)
            return HttpResponseRedirect('/quotation/staff_air/create/')

        elif form.cleaned_data['type'] == 'Sea':
            self.request.session['type'] = 'quote:create_sea'
            self.request.session['type_name'] = 'Sea'
            self.request.session['owner'] = form.cleaned_data['owner'].id
            form.instance.type = 'Quote_Sea'
            # super().form_valid(form)
            return HttpResponseRedirect('/quotation/staff_sea/create/')

        elif form.cleaned_data['type'] == 'Road':
            self.request.session['type'] = 'quote:create_road'
            self.request.session['type_name'] = 'Road'
            self.request.session['owner'] = form.cleaned_data['owner'].id
            form.instance.type = 'Quote_Road'
            # super().form_valid(form)
            return HttpResponseRedirect('/quotation/staff_road/create/')

        elif form.cleaned_data['type'] == 'Warehouse':
            self.request.session['type'] = 'quote:create_warehouse'
            self.request.session['type_name'] = 'Warehouse'
            self.request.session['owner'] = form.cleaned_data['owner'].id
            form.instance.type = 'Quote_Warehouse'
            # super().form_valid(form)
            return HttpResponseRedirect('/quotation/staff_warehouse/create/')
            
        # form.instance.owner = self.request.user
        # return super().form_valid(form)

#create sea quote client
class QuoteCreateView_Sea(CreateView):
    model = Quote_Sea
    fields = ['incoterm','other_vas','Country_of_Origin','Country_of_Destination','cargo_description','container_size','Nature_of_Cargo','special_delivery', 'Gross_Weight']
    template_name = 'createsea.html'
    success_url = '/quotation/list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Quote'
        context['type'] = 'Sea'
        print(context['type'])
        return context
    

    # @eye
    def form_valid(self, form):
        if self.request.user.is_staff:
            owner_id = self.request.session['owner']
            form.instance.owner = Account.objects.get(id=owner_id)
        else:
            form.instance.owner = self.request.user
        form.instance.quote_serial_no = random_serial_no()
        form.instance.quote_type = self.request.session['type_name']
        super().form_valid(form)
        if self.request.user.is_staff:
            return HttpResponseRedirect('/quotation/staff/list/')
        else:
            return HttpResponseRedirect('/quotation/list')

#create sea quote staff
class QuoteCreateViewStaff_Sea(CreateView):
    model = Quote_Sea
    fields = ['incoterm','other_vas','Country_of_Origin','Country_of_Destination','cargo_description','container_size','Nature_of_Cargo','special_delivery']
    template_name = 'createsea_staff.html'
    success_url = '/quotation/staff/list/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Quote'
        context['type'] = 'Sea'
        print(context['type'])
        return context

    # @eye
    def form_valid(self, form):
        if self.request.user.is_staff:
            owner_id = self.request.session['owner']
            form.instance.owner = Account.objects.get(id=owner_id)
        else:
            form.instance.owner = self.request.user
        form.instance.quote_serial_no = random_serial_no()
        form.instance.quote_type = self.request.session['type_name']
        return super().form_valid(form)

#create air quote client
class QuoteCreateView_Air(CreateView):
    model = Quote_Air
    fields = ['incoterm','other_vas','Country_of_Origin','Country_of_Destination','collection_address','cargo_description','Nature_of_Cargo','special_delivery','cargo_weight','Volume_CBM']
    template_name = 'createair.html'
    success_url = '/quotation/list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Quote'
        context['type'] = 'Air'
        return context

    def form_valid(self, form):
        if self.request.user.is_staff:
            owner_id = self.request.session['owner']
            form.instance.owner = Account.objects.get(id=owner_id)
        else:
            form.instance.owner = self.request.user
        form.instance.quote_serial_no = random_serial_no()
        form.instance.quote_type = self.request.session['type_name']
        super().form_valid(form)
        if self.request.user.is_staff:
            return HttpResponseRedirect('/quotation/staff/list/')
        else:
            return HttpResponseRedirect('/quotation/list')

#create air quote staff
class QuoteCreateViewStaff_Air(CreateView):
    model = Quote_Air
    fields = ['incoterm','other_vas','Country_of_Origin','Country_of_Destination','collection_address','cargo_description','Nature_of_Cargo','special_delivery','cargo_weight','Volume_CBM']
    template_name = 'createair_staff.html'
    success_url = '/quotation/staff/list/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Quote'
        context['type'] = 'Air'
        return context

    def form_valid(self, form):
        if self.request.user.is_staff:
            owner_id = self.request.session['owner']
            form.instance.owner = Account.objects.get(id=owner_id)
        else:
            form.instance.owner = self.request.user
        form.instance.quote_serial_no = random_serial_no()
        form.instance.quote_type = self.request.session['type_name']
        super().form_valid(form)
        return HttpResponseRedirect('/quotation/staff/list/')

#create road quote client
class QuoteCreateView_Road(CreateView):
    model = Quote_Road
    fields = ['Truck_Size','cargo_weight','Volume_CBM','incoterm', 'Additional_Information', 'collection_address','delivery_address']
    template_name = 'createroad.html'
    success_url = '/quotation/list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Quote'
        context['type'] = 'Road'
        return context

    def form_valid(self, form):
        if self.request.user.is_staff:
            owner_id = self.request.session['owner']
            form.instance.owner = Account.objects.get(id=owner_id)
        else:
            form.instance.owner = self.request.user
        form.instance.quote_serial_no = random_serial_no()
        form.instance.quote_type = self.request.session['type_name']
        super().form_valid(form)
        if self.request.user.is_staff:
            return HttpResponseRedirect('/quotation/staff/list/')
        else:
            return HttpResponseRedirect('/quotation/list')

#create road quote staff
class QuoteCreateViewStaff_Road(CreateView):
    model = Quote_Road
    fields = ['Truck_Size','cargo_weight','Volume_CBM','incoterm', 'Additional_Information', 'collection_address','delivery_address']
    template_name = 'createroad_staff.html'
    success_url = '/quotation/staff/list/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Quote'
        context['type'] = 'Road'
        return context

    def form_valid(self, form):
        if self.request.user.is_staff:
            owner_id = self.request.session['owner']
            form.instance.owner = Account.objects.get(id=owner_id)
        else:
            form.instance.owner = self.request.user
        form.instance.quote_serial_no = random_serial_no()
        form.instance.quote_type = self.request.session['type_name']
        return super().form_valid(form)

#create warehouse quote client
class QuoteCreateView_Warehouse(CreateView):
    model = Quote_Warehouse
    fields = ['cargo_description','cargo_weight','cargo_dimension_length','cargo_dimension_width','cargo_dimension_height','special_delivery']
    template_name = 'createwarehouse.html'
    success_url = '/quotation/list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Quote'
        context['type'] = 'Warehouse'
        return context

    def form_valid(self, form):
        if self.request.user.is_staff:
            owner_id = self.request.session['owner']
            form.instance.owner = Account.objects.get(id=owner_id)
        else:
            form.instance.owner = self.request.user
        form.instance.quote_serial_no = random_serial_no()
        form.instance.quote_type = self.request.session['type_name']
        super().form_valid(form)
        if self.request.user.is_staff:
            return HttpResponseRedirect('/quotation/staff/list/')
        else:
            return HttpResponseRedirect('/quotation/list')

#create warehouse quote staff
class QuoteCreateViewStaff_Warehouse(CreateView):
    model = Quote_Warehouse
    fields = ['cargo_description','cargo_weight','cargo_dimension_length','cargo_dimension_width','cargo_dimension_height','special_delivery']
    template_name = 'createwarehouse_staff.html'
    success_url = '/quotation/staff/list/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Quote'
        context['type'] = 'Warehouse'
        return context

    def form_valid(self, form):
        if self.request.user.is_staff:
            owner_id = self.request.session['owner']
            form.instance.owner = Account.objects.get(id=owner_id)
        else:
            form.instance.owner = self.request.user
        form.instance.quote_serial_no = random_serial_no()
        form.instance.quote_type = self.request.session['type_name']
        return super().form_valid(form)

#list quotation
class QuoteListView(ListView):
    model = Quote_App
    
    # @eye
    def get_queryset(self):
        return Quote_App.objects.filter(owner=self.request.user)

    # @eye
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

# @eye
def detailed_quote(request, quote_serial,quote_type,pk,incoterm):
    #check group session
    if quote_type == 'Warehouse':
        current_group = request.session['currentgroup']
        request.session['pk'] = str(pk)
        request.session['quote_serial'] = str(quote_serial)
        Quote_id = Quote_Warehouse.objects.get(quote_serial_no=quote_serial)
        request.session['quote_id'] = str(Quote_id.pk)
        request.session['incoterm'] = str(incoterm)

    else:
        current_group = request.session['currentgroup']
        request.session['pk'] = str(pk)
        request.session['quote_serial'] = str(quote_serial)
        Quote_id = Quote.objects.get(quote_serial_no=quote_serial)
        request.session['quote_id'] = str(Quote_id.pk)
        request.session['incoterm'] = str(incoterm)

    if quote_type == 'Sea':
        quote = Quote.objects.get(quote_serial_no=quote_serial)
        quote_sea_detail = Quote_Sea.objects.get(quote_serial_no=quote_serial)
        quote_app = Quote_App.objects.get(quote_serial_no=quote_serial)

        if current_group == "client":
            #Object does not exist
            try:
                client_pricing = Staff_Pricing_Quotation.objects.get(quotation=quote_app)
            except Staff_Pricing_Quotation.DoesNotExist:
                client_pricing = None
            return render(request, 'quote_detailed_sea.html', {'quote':quote,'quote_detail':quote_sea_detail,'quote_app':quote_app,'client_pricing':client_pricing})
        else:
            return render(request, 'quote_detailed_sea_staff.html', {'pk':pk,'quote':quote,'quote_detail':quote_sea_detail})
        
    elif quote_type == 'Air':
        quote = Quote.objects.get(quote_serial_no=quote_serial)
        quote_air_detail = Quote_Air.objects.get(quote_serial_no=quote_serial)
        quote_app = Quote_App.objects.get(quote_serial_no=quote_serial)

        if current_group == "client":
            try:
                client_pricing = Staff_Pricing_Quotation.objects.get(quotation=quote_app)
            except Staff_Pricing_Quotation.DoesNotExist:
                client_pricing = None
            return render(request, 'quote_detailed_air.html', {'quote':quote,'quote_detail':quote_air_detail,'quote_app':quote_app,'client_pricing':client_pricing})
            
        else:
            return render(request, 'quote_detailed_air_staff.html', {'quote':quote,'quote_detail':quote_air_detail})

    elif quote_type == 'Road':
        quote = Quote.objects.get(quote_serial_no=quote_serial)
        quote_road_detail = Quote_Road.objects.get(quote_serial_no=quote_serial)
        quote_app = Quote_App.objects.get(quote_serial_no=quote_serial)

        if current_group == "client":
            try:
                client_pricing = Staff_Pricing_Quotation.objects.get(quotation=quote_app)
            except Staff_Pricing_Quotation.DoesNotExist:
                client_pricing = None
            return render(request, 'quote_detailed_road.html', {'quote':quote,'quote_detail':quote_road_detail,'quote_app':quote_app,'client_pricing':client_pricing})
        else:
            return render(request, 'quote_detailed_road_staff.html', {'quote':quote,'quote_detail':quote_road_detail})

    elif quote_type == 'Warehouse':
        quote_warehouse_detail = Quote_Warehouse.objects.get(quote_serial_no=quote_serial)
        quote_app = Quote_App.objects.get(quote_serial_no=quote_serial)
        if current_group == "client":
            try:
                client_pricing = Staff_Pricing_Quotation.objects.get(quotation=quote_app)
            except Staff_Pricing_Quotation.DoesNotExist:
                client_pricing = None
            return render(request, 'quote_detailed_warehouse.html', {'quote_detail':quote_warehouse_detail,'quote_app':quote_app,'client_pricing':client_pricing})
        else:
            return render(request, 'quote_detailed_warehouse_staff.html', {'quote_detail':quote_warehouse_detail})


#staff quote list
class StaffQuoteListView(ListView):
    model = Quote_App
    template_name = 'quote_list_staff.html'

    def get_queryset(self):
        return Quote_App.objects.filter(status='pending')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List Quotation'
        return context

#staff add pricing
@eye
# @login_required
# @snoop
def staff_Add_Pricing(request):
    section = request.POST.get("section")
    quote_id = request.session['quote_id']
    quote_app_id = request.session['pk']
    agent_name = request.POST.get("agent_name")
    incoterms = request.session['incoterm']

    #quote app result set
    quote_app = Quote_App.objects.get(pk=quote_app_id)
    
    #staff pricing result set
    quote_pricing = Staff_Pricing_Quotation.objects.filter(quotation=quote_app)

    #initial data
    quote_pricing_initial = None
    if quote_pricing.count() > 0:
        quote_pricing_initial = Staff_Pricing_Quotation.objects.get(quotation=quote_app)

    if section == "agent":
        return render(request, 'sections/section_Agent.html',{'initial':quote_pricing_initial})

    if section == 'sectionA':
        if quote_pricing.exists():
            staff_pricing = Staff_Pricing_Quotation.objects.get(quotation=quote_app)
            staff_pricing.agent_name = agent_name
            staff_pricing.save()
        else:
            staff_pricing = Staff_Pricing_Quotation(quotation=quote_app,agent_name=agent_name)
            staff_pricing.save()

        if incoterms == "FOB":
            return render(request,'sections/sectionB.html',{'initial':quote_pricing_initial})
        elif incoterms == "CFR":
            return render(request,'sections/sectionC.html',{'initial':quote_pricing_initial})
        elif incoterms == "EX" or incoterms == "DAP":
            return render(request, 'sections/sectionA.html',{'initial':quote_pricing_initial})

        return render(request, 'sections/sectionA.html',{'initial':quote_pricing_initial})

    elif section == 'sectionB':
        staff_pricing = Staff_Pricing_Quotation.objects.get(quotation=quote_app)
        origin_haulage_bp = request.POST.get("origin_haulage_bp")
        origin_haulage_sp = request.POST.get("origin_haulage_sp")
        origin_haulage_margin = request.POST.get("origin_haulage_margin")

        staff_pricing.buying_origin_haulage = origin_haulage_bp
        staff_pricing.selling_origin_haulage = origin_haulage_sp
        staff_pricing.margin_origin_haulage = origin_haulage_margin

        customs_bp = request.POST.get("customs_bp")
        customs_sp = request.POST.get("customs_sp")
        customs_margin = request.POST.get("customs_margin")

        staff_pricing.buying_customs_documentation = customs_bp
        staff_pricing.selling_customs_documentation = customs_sp
        staff_pricing.margin_customs_documentation = customs_margin

        terminal_bp = request.POST.get("terminal_bp")
        terminal_sp = request.POST.get("terminal_sp")
        terminal_margin = request.POST.get("terminal_margin")

        staff_pricing.buying_origin_terminal_handling = terminal_bp
        staff_pricing.selling_origin_terminal_handling = terminal_sp
        staff_pricing.margin_origin_terminal_handling = terminal_margin

        airport_bp = request.POST.get("airport_bp")
        airport_sp = request.POST.get("airport_sp")
        airport_margin = request.POST.get("airport_margin")

        staff_pricing.buying_airport_charges = airport_bp
        staff_pricing.selling_airport_charges = airport_sp
        staff_pricing.margin_airport_charges = airport_margin

        other_charges_bp = request.POST.get("other_bp")
        other_charges_sp = request.POST.get("other_sp")
        other_margin = request.POST.get("other_margin")

        staff_pricing.buying_other_charges_A = other_charges_bp
        staff_pricing.selling_other_charges_A = other_charges_sp
        staff_pricing.margin_other_charges_A = other_margin

        buying_total_origin = request.POST.get("totals_bp_A")
        selling_total_origin = request.POST.get("totals_sp_A")
        margin_total_origin = request.POST.get("totals_margin_A")

        staff_pricing.buying_total_A = buying_total_origin
        staff_pricing.selling_total_A = selling_total_origin
        staff_pricing.margin_total_A = margin_total_origin 

        staff_pricing.save()
        return render(request, 'sections/sectionB.html',{'initial':quote_pricing_initial})

    elif section == 'sectionC':
        staff_pricing = Staff_Pricing_Quotation.objects.get(quotation=quote_app)
        freight_bp = request.POST.get("freight_bp")
        freight_sp = request.POST.get("freight_sp")
        freight_margin = request.POST.get("freight_margin")

        staff_pricing.buying_freight_cost = freight_bp
        staff_pricing.selling_freight_cost = freight_sp
        staff_pricing.margin_freight_cost = freight_margin

        other_freight_bp = request.POST.get("other_freight_bp")
        other_freight_sp = request.POST.get("other_freight_sp")
        other_freight_margin = request.POST.get("other_freight_margin")

        staff_pricing.buying_other_freight_charges = other_freight_bp
        staff_pricing.selling_other_freight_charges = other_freight_sp
        staff_pricing.margin_other_freight_charges = other_freight_margin

        total_bp_B = request.POST.get("total_bp_B")
        total_sp_B = request.POST.get("total_sp_B")
        total_margin_B = request.POST.get("total_margin_B")

        staff_pricing.buying_total_B = total_bp_B
        staff_pricing.selling_total_B = total_sp_B
        staff_pricing.margin_total_B = total_margin_B
        
        staff_pricing.save()

        if request.session['incoterm'] == "DAP":
            return render(request,'sections/sectionC.html',{'initial':quote_pricing_initial})
        else:
            return render(request, 'sections/sectionC.html',{'initial':quote_pricing_initial})
        
    elif section == 'sectionD':
        staff_pricing = Staff_Pricing_Quotation.objects.get(quotation=quote_app)
        handling_bp = request.POST.get("handling_bp")
        handling_sp = request.POST.get("handling_sp")
        handling_margin = request.POST.get("handling_margin")

        staff_pricing.buying_terminal_handling = handling_bp
        staff_pricing.selling_terminal_handling = handling_sp
        staff_pricing.margin_terminal_handling = handling_margin
        
        agency_fee_bp = request.POST.get("agency_fee_bp")
        agency_fee_sp = request.POST.get("agency_fee_sp")
        agency_fee_margin = request.POST.get("agency_fee_margin")

        staff_pricing.buying_agency_fee = agency_fee_bp
        staff_pricing.selling_agency_fee = agency_fee_sp
        staff_pricing.margin_agency_fee = agency_fee_margin

        transport_delivery_fee_bp = request.POST.get("transport_delivery_fee_bp")
        transport_delivery_fee_sp = request.POST.get("transport_delivery_fee_sp")
        transport_delivery_fee_margin = request.POST.get("transport_delivery_margin")

        staff_pricing.buying_transport_delivery = transport_delivery_fee_bp
        staff_pricing.selling_transport_delivery = transport_delivery_fee_sp
        staff_pricing.margin_transport_delivery = transport_delivery_fee_margin

        other_delivery_fee_bp = request.POST.get("other_delivery_fee_bp")
        other_delivery_fee_sp = request.POST.get("other_delivery_fee_sp")
        other_delivery_fee_margin = request.POST.get("other_margin")

        staff_pricing.buying_other_destination_charges = other_delivery_fee_bp
        staff_pricing.selling_other_destination_charges = other_delivery_fee_sp
        staff_pricing.margin_other_destination_charges = other_delivery_fee_margin

        
        total_bp_C = request.POST.get("total_bp_C")
        total_sp_C = request.POST.get("total_sp_C")
        total_margin_C = request.POST.get("total_margin_C")

        staff_pricing.buying_total_C = total_bp_C
        staff_pricing.selling_total_C = total_sp_C
        staff_pricing.margin_total_C = total_margin_C

        staff_pricing.save()

        #load taxes
        taxes = Taxes.objects.all().values()
        print(taxes)
        if request.session['incoterm'] == "DAP":
            return render(request,'sections/sectionE.html',{'initial':quote_pricing_initial})
        else:
            return render(request, 'sections/sectionD.html',{"taxes":taxes,'initial':quote_pricing_initial})

    elif section == 'sectionE':
        staff_pricing = Staff_Pricing_Quotation.objects.get(quotation=quote_app)
        
        hp_bp = request.POST.get("hs_bp")
        staff_pricing.hs_code_bp = hp_bp

        fob_bp = request.POST.get("fob_bp")
        staff_pricing.fob_value_bp = fob_bp

        freight_bp = request.POST.get("freight_fee_bp")
        #freight_sp = request.POST.get("freight_fee_sp")
        #freight_margin = request.POST.get("freight_fee_margin")
        staff_pricing.freight_charges_bp = freight_bp
        #staff_pricing.freight_charges_sp = freight_sp
        #staff_pricing.freight_charges_margin = freight_margin

        insurance_bp = request.POST.get("insurance_fee_bp")
        #insurance_sp = request.POST.get("insurance_fee_sp")
        #insurance_margin = request.POST.get("insurance_fee_margin")
        staff_pricing.insurance_bp = insurance_bp
        #staff_pricing.insurance_sp = insurance_sp
        #staff_pricing.insurance_margin = insurance_margin

        customs_bp = request.POST.get("customs_fee_bp")
        #customs_sp = request.POST.get("customs_fee_sp")
        #customs_margin = request.POST.get("customs_fee_margin")
        staff_pricing.customs_value_bp = customs_bp
        #staff_pricing.customs_value_sp = customs_sp
        #staff_pricing.customs_value_margin = customs_margin

        #totals D
        staff_pricing.buying_total_D = request.POST.get("total_bp_d")
        #staff_pricing.selling_total_D = request.POST.get("total_sp_d")
        #staff_pricing.margin_total_D = request.POST.get("total_margin_d")

        staff_pricing.import_duty_principal = request.POST.get("import_duty_principal")
        staff_pricing.import_duty = request.POST.get("import_duty")

        staff_pricing.excise_duty_principal = request.POST.get("excise_duty_principal")
        staff_pricing.excise_duty = request.POST.get("excise_duty")

        staff_pricing.vat_principal = request.POST.get("vat_principal")
        staff_pricing.vat = request.POST.get("vat")

        staff_pricing.railway_levy_principal = request.POST.get("railway_principal")
        staff_pricing.railway_levy = request.POST.get("railway_levy")

        staff_pricing.idf_fee_principal = request.POST.get("idf_principal")
        staff_pricing.idf_duty = request.POST.get("idf_duty")

        staff_pricing.levies_principal = request.POST.get("levies_principal")
        staff_pricing.levies = request.POST.get("levies")
        staff_pricing.total_tax = request.POST.get("total_tax")
        # staff_pricing.status = 'review'
        staff_pricing.save()

        #grand total
        staff_pricing.grand_total_bp = int(staff_pricing.buying_total_A) + int(staff_pricing.buying_total_B) + int(staff_pricing.buying_total_C) + int(staff_pricing.buying_total_D)
        staff_pricing.grand_total_sp = int(staff_pricing.selling_total_A) + int(staff_pricing.selling_total_B) + int(staff_pricing.selling_total_C) + int(staff_pricing.selling_total_D)
        staff_pricing.grand_total_margin = int(staff_pricing.margin_total_A) + int(staff_pricing.margin_total_B) + int(staff_pricing.margin_total_C) + int(staff_pricing.margin_total_D)
        staff_pricing.save()
        return render(request, 'sections/sectionE.html', {'data': staff_pricing,'initial':quote_pricing_initial})

    elif section == 'sectionF':
        #change status to review
        staff_pricing = Staff_Pricing_Quotation.objects.get(quotation=quote_app)
        staff_pricing.status = 'review'
        staff_pricing.save()

        #change status of quotation
        quote_app.status = 'review'
        quote_app.save()
        return render(request, 'sections/sectionF.html', {'data': staff_pricing,'initial':quote_pricing_initial})

def view_Staff_Pricing_List(request, pk=None):
    staff_pricing = Staff_Pricing_Quotation.objects.all().exclude(status='pending')
    return render(request, 'quote_pricing_staff.html', {'data': staff_pricing})

# @eye
def view_Staff_Pricing_Detailed(request, pk=None):
    current_group = request.user.groups.filter(name='Admins').exists()
    if current_group == True:
        request.session["is_admin"] = True
    staff_pricing = Staff_Pricing_Quotation.objects.get(id=pk)
    return render(request, 'quote_pricing_detailed_staff.html', {'data': staff_pricing})

# @snoop
def adminApproval(request):
    staff_pricing_id = request.POST.get("staff_pricing_id")
    staff_pricing = Staff_Pricing_Quotation.objects.get(id=staff_pricing_id)

    status = request.POST.get("approval_status")
    staff_pricing.status = status
    staff_pricing.save()
    
    #get quote id
    quote_id = staff_pricing.quotation.id

    if status == "approved":
        #change status of quotation
        quote_app = Quote_App.objects.get(id=quote_id)
        quote_app.status = 'approved_admin'
        quote_app.save()
        messages.success(request, 'Quotation Approved')
    else:
        quote_app = Quote_App.objects.get(id=quote_id)
        quote_app.status = 'pending'
        quote_app.save()
        messages.info(request, 'Quotation Rejected')
    return redirect('quote:staff_view_pricing')

def clientApproval(request):
    quote_id = request.POST.get("quote_id")
    quote_app = Quote_App.objects.get(id=quote_id)
    status = request.POST.get("approval_status")
    quote_app.status = status
    quote_app.save()
    if status == "approved":
        messages.success(request, 'Quotation Approved')
    else:
        messages.info(request, 'Quotation Rejected')
    return redirect('quote:list')

#download pdf pricing using pdfkit
def download_pdf_pricing(request, quote_app=None):
    staff_pricing = Staff_Pricing_Quotation.objects.get(quotation=quote_app)
    html = render_to_string('pdf_pricing.html', {'data': staff_pricing})
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None
    }
    pdf = pdfkit.from_string(html, False, options=options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="pricing.pdf"'
    return response