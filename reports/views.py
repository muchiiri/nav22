from urllib import request
from django.shortcuts import render,HttpResponse
from shipments.models import *
from accounts.models import *
import os
import mimetypes
import pdfkit
from django.template import loader
from datetime import date
from datetime import datetime

# Create your views here.
def report(request):
    all = request.POST.get("all")
    road = request.POST.get("road")
    sea = request.POST.get("sea")
    air = request.POST.get("air")

    data_road = None
    data_sea = None
    data_air = None
    freightforward = None

    if all:
        data_road = road_report(request)
        data_sea = sea_report(request)
        data_air = air_report(request)
        print("all")
    elif road and sea:
        data_road = road_report(request)
        data_sea = sea_report(request)
        print("road & sea")
    elif road and air:
        data_road = road_report(request)
        data_air = air_report(request)
        print("road & air")
    elif sea and air:
        data_sea= sea_report(request)
        data_air= air_report(request)
        print("sea & air")
    elif road:
        data_road = road_report(request)
        print("road")
    elif sea:
        data_sea = sea_report(request)
        print("sea")
    elif air:
        data_air = air_report(request)
        print("air")
    
    # Textual month, day and year
    today = date.today()
    d2 = today.strftime("%B %d, %Y")

    #current user
    currentuser = request.user
    
    uname = Account.objects.filter(email=currentuser)
    companyname = None

    for u in uname:
        companyname = u.company

    return render(request,"report.html",
    {"data_road":data_road,"data_sea":data_sea,"data_air":data_air,"today":d2,
    "companyname":companyname,"email":currentuser})

def road_report(request):
    currentuser = request.user
    road = RoadFreightShip.objects.filter(owner=currentuser)
    return road

def air_report(request):
    currentuser = request.user
    air = AirFreightShip.objects.filter(owner=currentuser)
    return air

def sea_report(request):
    currentuser = request.user
    sea = SeaFreightShip.objects.filter(owner=currentuser)
    return sea

def report_download_sea(request):
    # datetime object containing current date and time
    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")

    input_filename = 'download_report.html'
    output_filename = f'reports/seareports/seashipment_{dt_string}.pdf'

    # Textual month, day and year
    today = date.today()
    d2 = today.strftime("%B %d, %Y")

     #current user
    currentuser = request.user
    uname = Account.objects.filter(email=currentuser)
    companyname = None

    for u in uname:
        companyname = u.company
        companyaddr = u.address

    data_sea = sea_report(request)

    #get update from staff
    for shipment in data_sea:
        freightforward = FreightForwarding.objects.filter(refno=shipment.refno)

    html = loader.render_to_string(input_filename, {'data_sea':data_sea,'today':d2,"companyname":companyname,"currentuser":currentuser,"companyaddr":companyaddr,
    "freightforward":freightforward})
    
    output= pdfkit.from_string(html, output_path=output_filename)
    
    filename = f"/reports/seareports/seashipment_{dt_string}.pdf"
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = BASE_DIR + filename 
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = f"attachment; filename= seashipment_{dt_string}.pdf"

    return response

def report_download_road(request):
    # datetime object containing current date and time
    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")

    input_filename = 'download_report.html'
    output_filename = f'reports/roadreports/roadshipment_{dt_string}.pdf'

    # Textual month, day and year
    today = date.today()
    d2 = today.strftime("%B %d, %Y")

     #current user
    currentuser = request.user
    uname = Account.objects.filter(email=currentuser)
    companyname = None

    for u in uname:
        companyname = u.company
        companyaddr = u.address

    data_road = road_report(request)

    html = loader.render_to_string(input_filename, {'data_road':data_road,'today':d2,"companyname":companyname,"currentuser":currentuser,"companyaddr":companyaddr})
    output= pdfkit.from_string(html, output_path=output_filename)
    
    filename = f"/reports/roadreports/roadshipment_{dt_string}.pdf"
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = BASE_DIR + filename 
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = f"attachment; filename= roadshipment_{dt_string}.pdf"

    return response

def report_download_air(request):
    # datetime object containing current date and time
    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")

    input_filename = 'download_report.html'
    output_filename = f'reports/airreports/airshipment_{dt_string}.pdf'

    # Textual month, day and year
    today = date.today()
    d2 = today.strftime("%B %d, %Y")

     #current user
    currentuser = request.user
    uname = Account.objects.filter(email=currentuser)
    companyname = None

    for u in uname:
        companyname = u.company
        companyaddr = u.address

    data_air = air_report(request)

    html = loader.render_to_string(input_filename, {'data_air':data_air,'today':d2,"companyname":companyname,"currentuser":currentuser,"companyaddr":companyaddr})
    output= pdfkit.from_string(html, output_path=output_filename)
    
    filename = f"/reports/airreports/airshipment_{dt_string}.pdf"
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = BASE_DIR + filename 
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = f"attachment; filename= airshipment_{dt_string}.pdf"

    return response

def report_template(request):
    return render(request,"download_report.html")