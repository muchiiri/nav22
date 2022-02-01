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
    # all = request.POST.get("all")
    # road = request.POST.get("road")
    # sea = request.POST.get("sea")
    # air = request.POST.get("air")
    shippingstatus = request.POST.get("shippingstatus")
    request.session["shippingstatus"] = shippingstatus

    data_road = None
    data_sea = None
    data_air = None
    freightforward = None

    data_road = road_report(request)
    data_sea = sea_report(request)
    data_air = air_report(request)

    # if all:
    #     data_road = road_report(request)
    #     data_sea = sea_report(request)
    #     data_air = air_report(request)
    #     print("all")
    # elif road and sea:
    #     data_road = road_report(request)
    #     data_sea = sea_report(request)
    #     print("road & sea")
    # elif road and air:
    #     data_road = road_report(request)
    #     data_air = air_report(request)
    #     print("road & air")
    # elif sea and air:
    #     data_sea= sea_report(request)
    #     data_air= air_report(request)
    #     print("sea & air")
    # elif road:
    #     data_road = road_report(request)
    #     print("road")
    # elif sea:
    #     data_sea = sea_report(request)
    #     print("sea")
    # elif air:
    #     data_air = air_report(request)
    #     print("air")
    
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
    type = request.session["shippingstatus"]
    road = RoadFreightShip.objects.filter(owner=currentuser,shippingstatus=type)
    print(type)
    return road

def air_report(request):
    currentuser = request.user
    type = request.session["shippingstatus"]
    air = AirFreightShip.objects.filter(owner=currentuser,shippingstatus=type)
    return air

def sea_report(request):
    currentuser = request.user
    type = request.session["shippingstatus"]
    sea = SeaFreightShip.objects.filter(owner=currentuser,shippingstatus=type)
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

def report_summary_charts(request):
    context = {}
    complete = 0
    incomplete = 0
    seano = 0
    airno = 0
    roadno = 0

    road_shipment = road_report(request)
    sea_shipment = sea_report(request)
    air_shipment = air_report(request)


    #loop thru shipments to get complete and incomplete shipments
    for r in road_shipment:
        roadno = roadno + 1
        if r.shippingstatus == "Completed":
            complete = complete + 1
        else:
            incomplete = incomplete + 1

    for s in sea_shipment:
        seano = seano + 1
        if s.shippingstatus == "Completed":
            complete = complete + 1
        else:
            incomplete = incomplete + 1
    
    for a in air_shipment:
        airno = airno + 1
        if r.shippingstatus == "Completed":
            complete = complete + 1
        else:
            incomplete = incomplete + 1

    context ={
        "complete":complete,
        "incomplete":incomplete,
        "seano":seano,
        "airno":airno,
        "roadno":roadno,
    }

    return render(request,"summary_report.html",{"context":context})