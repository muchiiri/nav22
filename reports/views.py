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
import time
# Create your views here.

def report(request):
    if request.method == 'POST':
        shippingstatus = request.POST.get("shippingstatus")
        request.session["shippingstatus"] = shippingstatus
    else:
        request.session["shippingstatus"] = None
    request.session["report_type"] = "table_report"
    data_road = None
    data_sea = None
    data_air = None
    freightforward = None

    #check group of user
    user = request.user

    #if client else if staff
    if user.groups.filter(name='Ogl Clients').exists():
        data_road = road_report(request)
        data_sea = sea_report(request)
        data_air = air_report(request)
    else:
        data_road = fielduser_road_report(request)
        data_sea = fielduser_sea_report(request)
        data_air = fielduser_air_report(request)
    
    # Textual month, day and year
    today = date.today()
    d2 = today.strftime("%B %d, %Y")

    #current user
    currentuser = request.user
    
    uname = Account.objects.filter(email=currentuser)
    companyname = None

    for u in uname:
        companyname = u.company

    # get list of owners
    owners = []
    usergroup = Account.objects.filter(groups__name='Ogl Clients')
    usergrouplen = len(usergroup)
    for i in range(usergrouplen):
        owners.append(usergroup[i])

    #if client else if staff
    if user.groups.filter(name='Ogl Clients').exists():
        
        return render(request,"report.html",
        {"data_road":data_road,"data_sea":data_sea,"data_air":data_air,"today":d2,
        "companyname":companyname,"email":currentuser,"owners":owners})

    if user.groups.filter(name='Ogl_fielduser').exists():
        
        return render(request,"fielduser_report.html",
        {"data_road":data_road,"data_sea":data_sea,"data_air":data_air,"today":d2,
        "companyname":companyname,"email":currentuser,"owners":owners})
    
    

#client report
def road_report(request):
    currentuser = request.user
    
    if request.session["report_type"] == "table_report":
        type = request.session["shippingstatus"]

        #if client else if staff
        if currentuser.groups.filter(name='Ogl Clients').exists():
            road = RoadFreightShip.objects.filter(owner=currentuser,shippingstatus=type)
        else:
            owner = request.session["owner"]
            road = RoadFreightShip.objects.filter(staff=currentuser,shippingstatus=type,owner=owner)

        if not road and request.method == "POST":
            type = ""
            road = RoadFreightShip.objects.filter(owner=currentuser,shippingstatus=type)
    else:
        road = RoadFreightShip.objects.filter(owner=currentuser)
    return road

#fielduser report
def fielduser_road_report(request):
    currentuser = request.user
    owner = request.POST.get("owner")
    request.session["owner"] = owner


    if request.session["report_type"] == "table_report":
        type = request.session["shippingstatus"]
        road = RoadFreightShip.objects.filter(staff=currentuser,shippingstatus=type,owner=owner)
        if not road and request.method == "POST":
            type = ""
            road = RoadFreightShip.objects.filter(owner=currentuser,shippingstatus=type)
    else:
        road = RoadFreightShip.objects.filter(owner=currentuser)
    return road

#client report
def air_report(request):
    currentuser = request.user
    if request.session["report_type"] == "table_report":
        type = request.session["shippingstatus"]

        #if client else if staff
        if currentuser.groups.filter(name='Ogl Clients').exists():
            air = AirFreightShip.objects.filter(owner=currentuser,shippingstatus=type)
        else:
            owner = request.session["owner"]
            air = AirFreightShip.objects.filter(staff=currentuser,shippingstatus=type,owner=owner)
    else:
        air = AirFreightShip.objects.filter(owner=currentuser)
    return air

#fielduser report
def fielduser_air_report(request):
    currentuser = request.user
    owner = request.POST.get("owner")
    request.session["owner"] = owner

    if request.session["report_type"] == "table_report":
        type = request.session["shippingstatus"]
        air = AirFreightShip.objects.filter(staff=currentuser,shippingstatus=type,owner=owner)
    else:
        air = AirFreightShip.objects.filter(staff=currentuser)
    return air

#client report
def sea_report(request):
    currentuser = request.user
    if request.session["report_type"] == "table_report":
        type = request.session["shippingstatus"]
        
        #if client else if staff
        if currentuser.groups.filter(name='Ogl Clients').exists():
            sea = SeaFreightShip.objects.filter(owner=currentuser,shippingstatus=type)
            
            #in case sea queryset is empyt, also check shipping status with this spelling
            if not sea and request.method == "POST":
                sea = SeaFreightShip.objects.filter(owner=currentuser,shippingstatus="In Progress")
        else:
            owner = request.session["owner"]
            sea = SeaFreightShip.objects.filter(staff=currentuser,shippingstatus=type,owner=owner)
    else:
        sea = SeaFreightShip.objects.filter(owner=currentuser)
    
    return sea

#fielduser report
def fielduser_sea_report(request):
    currentuser = request.user
    owner = request.POST.get("owner")
    request.session["owner"] = owner

    if request.session["report_type"] == "table_report":
        type = request.session["shippingstatus"]
        sea = SeaFreightShip.objects.filter(staff=currentuser,shippingstatus=type,owner=owner)

        if not sea and request.method == "POST":
            type="In Progress"
            sea = SeaFreightShip.objects.filter(staff=currentuser,shippingstatus=type,owner=owner)
    else:
        sea = SeaFreightShip.objects.filter(owner=currentuser)
    return sea

#download pdf
def report_download_sea(request):
    currentuser = request.user
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

    #change method GET to POST
    request.method = "POST"
    
    data_sea = sea_report(request)
    # if currentuser.groups.filter(name='Ogl Clients').exists():    
    #     data_sea = sea_report(request)
    # else:
    #     print("Fielduser")
    #     data_sea = fielduser_sea_report(request)
    
    #get update from staff
    freightforward = None
    for shipment in data_sea:
        freightforward = FreightForwarding.objects.filter(refno=shipment.refno)
    
    html = loader.render_to_string(input_filename, {'data_sea':data_sea,'today':d2,"companyname":companyname,"currentuser":currentuser,"companyaddr":companyaddr,
    "freightforward":freightforward})
    
    time.sleep(1)
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
    time.sleep(1)
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
    
    #get update from staff
    freightforward = None
    for shipment in data_air:
        freightforward = FreightForwarding.objects.filter(refno=shipment.refno)

    html = loader.render_to_string(input_filename, {'data_air':data_air,'today':d2,"companyname":companyname,"currentuser":currentuser,"companyaddr":companyaddr,"freightforward":freightforward})
    time.sleep(1)
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
    request.session["report_type"] = "summary_report"
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
        if a.shippingstatus == "Completed":
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

def fielduser_report(request):
    # get list of owners for dropdown
    owners = []
    usergroup = Account.objects.filter(groups__name='Ogl Clients')
    usergrouplen = len(usergroup)
    for i in range(usergrouplen):
        owners.append(usergroup[i])
    return render(request,"fielduser_report.html",{"owners":owners})