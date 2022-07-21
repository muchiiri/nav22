from multiprocessing.dummy import current_process
from django.shortcuts import render
from urllib3 import HTTPResponse
from .models import Quotation,Quotation_Staff,Staff_Quotation,Admin_Quotation, Quotation_Air
from .forms import QuotationForm,StaffQuotationForm,AdminQuotationForm,ClientQuotationPricing,Quotation_Air

import random
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from accounts.models import Account
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect
import snoop
import json


#round robin staff quote allocation
def quote_staff_owner(request):
    fetch_staff = Quotation_Staff.objects.all()
    all_staff = {}
    staff_owner = None
    for user in fetch_staff.values():
        all_staff[user["staff_id"]]=user["quotations"]
    
    #get minimum value
    temp = min(all_staff.values())
    staff_owner = [key for key in all_staff if all_staff[key] == temp]
    return str(staff_owner[0])

# Create your views here.
def quote_type(request):
    current_user = request.user
    if request.method == "POST":
        quote_staff_owner(request)
        quote_form = QuotationForm(request.POST)
        
        for key in request.POST:
            print(key,request.POST[key])

        if quote_form.is_valid():
            record = quote_form.save(commit=False)
            record.owner = current_user
            staffid = quote_staff_owner(request)
            
            record.staff_owner = staffid
            record.save()

            #update quotation staff
            #add 1 to this staff
            quotation_staff = Quotation_Staff.objects.filter(staff=staffid)
            quotation_no = int(quotation_staff.values()[0]["quotations"]) + 1
            
            Quotation_Staff.objects.filter(staff = staffid).update(quotations = quotation_no)
            return HttpResponseRedirect(reverse('quotation:quote_list'))
        else:
            print(quote_form.errors)
            return render(request,"quotation_wizard_air.html",{"form":quote_form})

    else:
        random_number = random.randint(10,10000)
        quote_form = QuotationForm(initial={'quote_number':random_number})
        return render(request,"quote_type.html",{"form":quote_form})

#quote air
def quote_air(request):
    if request.method == "POST":
        quote_form = Quotation_Air(request.POST)
        if quote_form.is_valid():
            record = quote_form.save(commit=False)
            record.owner = request.user
            record.save()
            return HttpResponseRedirect(reverse('quotation:quote_list'))
        else:
            print(quote_form.errors)
            return render(request,"quotation_wizard_air.html",{"form":quote_form})
    else:
        quote_form = Quotation_Air()
        return render(request,"quotation_wizard_air.html",{"form":quote_form})

#client list quotations
def quote_list(request):
    current_user = request.user
    quote = Quotation.objects.filter(owner=current_user)
    quote_list = []
    
    for qot in quote:
        quote_list.append(qot)
    return render(request,"quote_list.html",{"quotes":quote_list})

# #client all list quotations
# def quote_list_all(request):
#     current_user = request.user
#     quote = Quotation.objects.all()
#     quote_list = []
    
#     for qot in quote:
#         quote_list.append(qot)
#     return render(request,"quote_list.html",{"quotes":quote_list})

#client detailed quotation
def quote_detailed(request,id):
    quote = Quotation.objects.filter(id=id)
    quote_values = quote.values()
    return render(request,"quote_detailed.html",{"quote":quote_values})

#client pricing: view quote pricing
def quote_pricing(request,quote_id,quote_incoterms):
    quotation = Staff_Quotation.objects.get(quotation=quote_id)
    print(quote_incoterms)
    initial = {
        "quotation":quotation.quotation,
        "agent_name":quotation.agent_name,
        "selling_origin_haulage":quotation.selling_origin_haulage,
        "selling_customs_documentation":quotation.selling_customs_documentation,
        "selling_origin_terminal_handling":quotation.selling_origin_terminal_handling,
        "selling_port_charges":quotation.selling_port_charges,
        "selling_other_charges":quotation.selling_other_charges,
        "selling_freight_cost":quotation.selling_freight_cost,
        "selling_other_freight_charges":quotation.selling_other_freight_charges,
        "selling_total_origin":quotation.selling_total_origin,
        "selling_terminal_handling":quotation.selling_terminal_handling,
        "selling_port_charges_dest":quotation.selling_port_charges_dest,
        "selling_agency_fee":quotation.selling_agency_fee,
        "selling_transport_delivery":quotation.selling_transport_delivery,
        "selling_other_destination_charges":quotation.selling_other_destination_charges,
        "selling_total_destination":quotation.selling_total_destination,
        "hs_code":quotation.hs_code,
        "fob_value":quotation.fob_value,
        "freight_charges":quotation.freight_charges,
        "insurance":quotation.insurance,
        "customs_value":quotation.customs_value,
        "sub_total_duties":quotation.sub_total_duties,
        "import_duty":quotation.import_duty,
        "excise_duty":quotation.excise_duty,
        "vat":quotation.vat,
        "railway_levy":quotation.railway_levy,
        "idf_fee":quotation.idf_fee,
        "levies":quotation.levies,
        "sub_total_taxes":quotation.sub_total_taxes,
        "total_tax":quotation.total_tax,
        "grand_total":quotation.grand_total,
    }
    
    quote_pricing = ClientQuotationPricing(initial=initial)
    return render(request,"quote_pricing.html",{"quote_pricing":quote_pricing,"quote_incoterms":quote_incoterms,"quote_id":quotation.quotation_id})

#staff quote list
def staff_quote_list(request):
    #query Quotation model
    staff_id = request.user.id
    quotation = Quotation.objects.filter(staff_owner=staff_id)

    return render(request,"staff/staff_quote_list.html",{"quotes":quotation,"sidebar":"true"})

#staff quote list all
def staff_quote_list_all(request):
    #query Quotation model
    staff_id = request.user.id
    quotation = Quotation.objects.all()
    return render(request,"staff/staff_quote_list.html",{"quotes":quotation,"sidebar":"true"})


#staff detailed quotation
def staff_quote_detailed(request,id):
    staff_id = request.user.id
    quote = Quotation.objects.get(id=id)

    if request.method == "POST":
        quote_pricing = StaffQuotationForm(request.POST)
        if quote_pricing.is_valid():
            record = quote_pricing.save(commit=False)
            record.status = "review"
            record.save()

            #update Quotation status
            quote.status = "review"
            quote.save()

    #query Staff Quotation
    quote_pricing = Staff_Quotation.objects.filter(quotation=id)

    status = None
    
    if quote_pricing.exists():
        initial = {
            'quotation': id,
            'agent_name': quote_pricing.values()[0]['agent_name'],
            'buying_origin_haulage': quote_pricing.values()[0]['buying_origin_haulage'],
            'selling_origin_haulage': quote_pricing.values()[0]['selling_origin_haulage'],
            'margin_origin_haulage': quote_pricing.values()[0]['margin_origin_haulage'],
            'buying_customs_documentation': quote_pricing.values()[0]['buying_customs_documentation'],
            'selling_customs_documentation': quote_pricing.values()[0]['selling_customs_documentation'],
            'margin_customs_documentation': quote_pricing.values()[0]['margin_customs_documentation'],
            'buying_origin_terminal_handling': quote_pricing.values()[0]['buying_origin_terminal_handling'],
            'selling_origin_terminal_handling': quote_pricing.values()[0]['selling_origin_terminal_handling'],
            'margin_origin_terminal_handling': quote_pricing.values()[0]['margin_origin_terminal_handling'],
            'buying_port_charges': quote_pricing.values()[0]['buying_port_charges'],
            'selling_port_charges': quote_pricing.values()[0]['selling_port_charges'],
            'margin_port_charges': quote_pricing.values()[0]['margin_port_charges'],
            'buying_other_charges': quote_pricing.values()[0]['buying_other_charges'],
            'selling_other_charges': quote_pricing.values()[0]['selling_other_charges'],
            'margin_other_charges': quote_pricing.values()[0]['margin_other_charges'],
            'buying_freight_cost': quote_pricing.values()[0]['buying_freight_cost'],
            'selling_freight_cost': quote_pricing.values()[0]['selling_freight_cost'],
            'margin_freight_cost': quote_pricing.values()[0]['margin_freight_cost'],
            'buying_other_freight_charges': quote_pricing.values()[0]['buying_other_freight_charges'],
            'selling_other_freight_charges': quote_pricing.values()[0]['selling_other_freight_charges'],
            'margin_other_freight_charges': quote_pricing.values()[0]['margin_other_freight_charges'],
            'buying_total_origin': quote_pricing.values()[0]['buying_total_origin'],
            'selling_total_origin': quote_pricing.values()[0]['selling_total_origin'],
            'margin_total_origin': quote_pricing.values()[0]['margin_total_origin'],
            'buying_terminal_handling': quote_pricing.values()[0]['buying_terminal_handling'],
            'selling_terminal_handling': quote_pricing.values()[0]['selling_terminal_handling'],
            'margin_terminal_handling': quote_pricing.values()[0]['margin_terminal_handling'],
            'buying_port_charges_dest': quote_pricing.values()[0]['buying_port_charges_dest'],
            'selling_port_charges_dest': quote_pricing.values()[0]['selling_port_charges_dest'],
            'margin_port_charges_dest': quote_pricing.values()[0]['margin_port_charges_dest'],
            'buying_agency_fee': quote_pricing.values()[0]['buying_agency_fee'],
            'selling_agency_fee': quote_pricing.values()[0]['selling_agency_fee'],
            'margin_agency_fee': quote_pricing.values()[0]['margin_agency_fee'],
            'buying_transport_delivery': quote_pricing.values()[0]['buying_transport_delivery'],
            'selling_transport_delivery': quote_pricing.values()[0]['selling_transport_delivery'],
            'margin_transport_delivery': quote_pricing.values()[0]['margin_transport_delivery'],
            'buying_other_destination_charges': quote_pricing.values()[0]['buying_other_destination_charges'],
            'selling_other_destination_charges': quote_pricing.values()[0]['selling_other_destination_charges'],
            'margin_other_destination_charges': quote_pricing.values()[0]['margin_other_destination_charges'],
            'buying_total_destination': quote_pricing.values()[0]['buying_total_destination'],
            'selling_total_destination': quote_pricing.values()[0]['selling_total_destination'],
            'margin_total_destination': quote_pricing.values()[0]['margin_total_destination'],
            'hs_code': quote_pricing.values()[0]['hs_code'],
            'fob_value': quote_pricing.values()[0]['fob_value'],
            'freight_charges': quote_pricing.values()[0]['freight_charges'],
            'insurance': quote_pricing.values()[0]['insurance'],
            'customs_value': quote_pricing.values()[0]['customs_value'],
            'sub_total_duties': quote_pricing.values()[0]['sub_total_duties'],
            'import_duty': quote_pricing.values()[0]['import_duty'],
            'excise_duty': quote_pricing.values()[0]['excise_duty'],
            'vat': quote_pricing.values()[0]['vat'],
            'railway_levy': quote_pricing.values()[0]['railway_levy'],
            'idf_fee': quote_pricing.values()[0]['idf_fee'],
            'levies': quote_pricing.values()[0]['levies'],
            'sub_total_taxes': quote_pricing.values()[0]['sub_total_taxes'],
            'total_tax': quote_pricing.values()[0]['total_tax'],
            'grand_total': quote_pricing.values()[0]['grand_total'],
        
        }
        status = "reviewed"

    else:
        initial={'quotation':id}
        status = "pending"

    #model form
    quote_id = quote.id
    staff_pricing_form = StaffQuotationForm(initial=initial)

    #check if approver has reviewed the quote
    quote_approver = Admin_Quotation.objects.filter(quotation=quote_id)
    
    if quote_approver.exists():
        initial_admin ={
            "status_admin":quote_approver[0].status_admin,
            "comment":quote_approver[0].comment
        }
    else:
        initial_admin = {
            "quotation":quote_id
        }
    admin_form = AdminQuotationForm(initial=initial_admin)
    

    return render(request,"staff/staff_quote_detailed.html",{"quote":quote,
    "staff_pricing_form":staff_pricing_form,"status":status,"admin_form":admin_form,"sidebar":"true"})

#admin approval of Quote pricing
def admin_review(request):
    if request.method == "POST":
        admin_form = AdminQuotationForm(request.POST)
        
        if admin_form.is_valid():
            admin_form.save()

        #change status of Quotation
        qid = request.POST.get("quotation")
        quote = Quotation.objects.get(id=qid)

        if request.POST.get("status_admin") == "approved":
            quote.status = "approved_admin"
            quote.save()


        #change status of Staff Quotation
        quote_staff = Staff_Quotation.objects.get(quotation=qid)
        quote_staff.status = request.POST.get("status_admin")
        quote_staff.save()

    return redirect(f"/quotation/staff_detailed/{qid}/")


#client decision
def client_decision(request):
    print(request.GET)
    quote_id = int(request.GET.get("id"))
    decision = request.GET.get("status")
    
    quote_status = Quotation.objects.get(id=quote_id)
    quote_status.status = decision
    quote_status.save()
    return HttpResponse("200")
