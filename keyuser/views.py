from django.shortcuts import render,redirect
from .forms import *
from accounts.models import *
from django.contrib.auth.decorators import login_required,user_passes_test
import random
from shipments.models import *

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
import datetime
# Create your views here.

# Create your views here.
def not_in_oglstaff_group(user):
	if user.groups.filter(name='Ogl_keyuser').exists():
		return True
	else:
		return False

@login_required
@user_passes_test(not_in_oglstaff_group,login_url='/client/')
def home(request):
    roadfreight = RoadFreightShip.objects.filter( staff= request.user)
    seafreight = SeaFreightShip.objects.filter( staff= request.user)
    airfreight = AirFreightShip.objects.filter( staff= request.user)

    rno = len(roadfreight)
    sno = len(seafreight)
    airno = len(airfreight)
    allno = rno+sno+airno
    return render(request,"index_fielduser.html",{"group":"staff","context":roadfreight,"context2":seafreight,"context3":airfreight,"rno":rno,"airno":airno,"sno":sno,"allno":allno,"sidebar":"true"})

def home2(request):
    roadfreight = RoadFreightShip.objects.filter( staff= request.user)
    seafreight = SeaFreightShip.objects.filter( staff= request.user)
    airfreight = AirFreightShip.objects.filter( staff= request.user)

    rno = len(roadfreight)
    sno = len(seafreight)
    airno = len(airfreight)
    allno = rno+sno+airno

    return render(request,"index_completed.html",{"group":"staff","context":roadfreight,
    "context2":seafreight,"context3":airfreight,"airno":airno,"sno":sno,"rno":rno,
    "allno":allno,"sidebar":"false"})

@login_required
def RoadFreightShip_view(request):
    context = {}
    #form = RoadFreightShipForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        form = RoadFreightShipForm(request.POST)
        form = form.save(commit=False)
        print(request.user)
        form.staff = request.user
        form.save()
        print(form)
        currentowner = request.POST['owner']
        
        email = EmailMessage(
            'Road Freight Shipment created',
            'Dear Customer, A new road freightship shipment has been created for you. Kindly login to Navicus360 system to view it. Thank you.',
            settings.EMAIL_HOST_USER,
            [str(currentowner)]
        )

        email.fail_silently = True
        email.send()

        messages.success(request,"Shipment created successfully, email has been sent to customer.")

        response = redirect('/keyuser')
        return response
        #return render(request,"index_fielduser.html")
    else:
        #import pdb;pdb.set_trace()
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")
        lastone = year[-1]
        lasttwo = year[-2]
        
        n = random.randint(1000, 99999)
        refno = "OGLRF"+str(lasttwo)+str(lastone)+str(n)
        form = RoadFreightShipForm()
        #import pdb;pdb.set_trace()
        # get list of owners
        owners = []
        usergroup = Account.objects.filter(groups__name='Ogl Clients')
        usergrouplen = len(usergroup)
        for i in range(usergrouplen):
            owners.append(usergroup[i])

    return render(request,"kcargoroad.html",{'form':form,'group':'staff','refno':refno,"sidebar":"true","owners":owners})

def AirFreightShip_view(request):
    context = {}
    #form = RoadFreightShipForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        form = AirFreightShipForm(request.POST)
        # import pdb; pdb.set_trace()
        form = form.save(commit=False)
        print(request.user)
        form.staff = request.user
        form.save()
        print(form)

        currentowner = request.POST['owner']
        
        email = EmailMessage(
            'Air Freight Shipment created',
            'Dear Customer, A new air freightship shipment has been created for you. Kindly login to Navicus360 system to view it. Thank you.',
            settings.EMAIL_HOST_USER,
            [str(currentowner)]
        )

        email.fail_silently = True
        email.send()
        messages.success(request,"Shipment created successfully, email has been sent to customer.")

        response = redirect('/keyuser')
        return response
        #return render(request,"index_fielduser.html")
    else:
        print(request.user)
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")
        lastone = year[-1]
        lasttwo = year[-2]
        
        n = random.randint(1000, 99999)
        refno = "OGLAF"+str(lasttwo)+str(lastone)+str(n)

        owners = []
        usergroup = Account.objects.filter(groups__name='Ogl Clients')
        usergrouplen = len(usergroup)
        for i in range(usergrouplen):
            owners.append(usergroup[i])

        form = AirFreightShipForm()


    return render(request,"kcargoair.html",{'form':form,'group':'staff','refno':refno,"sidebar":"true","owners":owners})

def SeaFreightShip_view(request):
    context = {}
    #form = RoadFreightShipForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        form = SeaFreightShipForm(request.POST)
        form = form.save(commit=False)
        print(request.user)
        form.staff = request.user
        form.save()
        print(form)

        currentowner = request.POST['owner']
        
        # email = EmailMessage(
        #     'Sea Freight Shipment created',
        #     'Dear Customer, A new sea freightship shipment has been created for you. Kindly login to Navicus360 system to view it. Thank you.',
        #     settings.EMAIL_HOST_USER,
        #     [str(currentowner)]
        # )

        # email.fail_silently = True
        # email.send()
        # messages.success(request,"Shipment created successfully, email has been sent to customer.")

        response = redirect('/keyuser')
        return response
        #return render(request,"index_fielduser.html")
    else:
        print(request.user)
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")
        lastone = year[-1]
        lasttwo = year[-2]
        
        n = random.randint(1000, 99999)
        refno = "OGLSF"+str(lasttwo)+str(lastone)+str(n)

        owners = []
        usergroup = Account.objects.filter(groups__name='Ogl Clients')
        usergrouplen = len(usergroup)
        for i in range(usergrouplen):
            owners.append(usergroup[i])
        form = SeaFreightShipForm()


    return render(request,"kcargosea.html",{'form':form,'group':'staff','refno':refno,"sidebar":"true","owners":owners})

@login_required
def editRoadFreigh(request,userid,refno):
    #userid = userid
    if request.method == "GET":
        RoadModelobject = RoadFreightShip.objects.get(id=userid)
        #import pdb;pdb.set_trace()
        return render(request,'edit.html',{'roadfreigh':RoadModelobject,'refno':refno})   
    else:
        print(userid)
        #import pdb;pdb.set_trace()
        form = RoadFreightShip.objects.get(id=userid)
        form.owner = request.POST.get("owner")
        form.billofnumber = request.POST.get("bill")
        form.incoterms = request.POST.get("incoterms")
        form.cargo_description = request.POST.get("desc")
        form.placeofloading = request.POST.get("load")
        form.placeofdelivery = request.POST.get("delivery")
        form.cargoload = request.POST.get("cload")
        form.save()
        
        

        #return render(request,'index_fielduser.html',{'success':'success'})
        return redirect(settings.BASEURL+"keyuser/")

@login_required
def editSeaFreigh(request,userid,refno):
    #userid = userid
    if request.method == "GET":
        SeaModelobject = SeaFreightShip.objects.get(id=userid)
        #import pdb;pdb.set_trace()
        return render(request,'edit.html',{'roadfreigh':SeaModelobject,'refno':refno})   
    else:
        print(userid)
        #import pdb;pdb.set_trace()
        form = SeaFreightShip.objects.get(id=userid)
        form.owner = request.POST.get("owner")
        form.billofnumber = request.POST.get("bill")
        form.incoterms = request.POST.get("incoterms")
        form.cargo_description = request.POST.get("desc")
        form.placeofloading = request.POST.get("load")
        form.placeofdelivery = request.POST.get("delivery")
        form.cargoload = request.POST.get("cload")
        form.save()
        

        #return render(request,'index_fielduser.html',{'success':'success'})
        return redirect(settings.BASEURL+"keyuser/")

@login_required
def editAirFreigh(request,userid,refno):
    #userid = userid
    if request.method == "GET":
        AirModelobject = AirFreightShip.objects.get(id=userid)
        #import pdb;pdb.set_trace()
        return render(request,'edit.html',{'roadfreigh':AirModelobject,'refno':refno})   
    else:
        print(userid)
        #import pdb;pdb.set_trace()
        form = AirFreightShip.objects.get(id=userid)
        form.owner = request.POST.get("owner")
        form.billofnumber = request.POST.get("bill")
        form.incoterms = request.POST.get("incoterms")
        form.cargo_description = request.POST.get("desc")
        form.placeofloading = request.POST.get("load")
        form.placeofdelivery = request.POST.get("delivery")
        form.cargoload = request.POST.get("cload")
        form.save()
        

        #return render(request,'index_fielduser.html',{'success':'success'})
        return redirect(settings.BASEURL+"keyuser/")


def view(request,uid,refno):
    userdetails_road = RoadFreightShip.objects.filter(id=uid)
    userdetails_sea = SeaFreightShip.objects.filter(id=uid)
    userdetails_air = AirFreightShip.objects.filter(id=uid)
    updateonshipments = FreightForwarding.objects.filter(refno=refno)
    return render(request,"kview.html",{"context":userdetails_road,"context2":userdetails_sea,"context3":userdetails_air,"updateonshipments":updateonshipments,"group":"staff","sidebar":"false"})

def view2(request,uid,refno):
    #userdetails_road = RoadFreightShip.objects.filter(id=uid)
    userdetails_sea = SeaFreightShip.objects.filter(id=uid)
    #import pdb;pdb.set_trace()
    updateonshipments = FreightForwarding.objects.filter(refno=refno)
    return render(request,"kview.html",{"context":userdetails_sea,"updateonshipments":updateonshipments,"group":"staff","sidebar":"false"})

def view3(request,uid,refno):
    #userdetails_road = RoadFreightShip.objects.filter(id=uid)
    userdetails_air = AirFreightShip.objects.filter(id=uid)
    #import pdb;pdb.set_trace()
    updateonshipments = FreightForwarding.objects.filter(refno=refno)
    return render(request,"kview.html",{"context":userdetails_air,"updateonshipments":updateonshipments,"group":"staff","sidebar":"false"})

    # This is the Key UserFreightForwding view to update shipments(Same as fielduser's)

@login_required
def FreightForwardingView(request):
    if request.method == "POST":
        form = FreightForwarding()
        form.refno = request.POST.get("refno")
        form.etd = request.POST.get("etd")
        form.eta = request.POST.get("eta")
        form.sailingstatus = request.POST.get("sailingstatus")
        form.update = request.POST.get("update")
        form.staffcomments = request.POST.get("staffcomments")
        form.save()

        

        currentrefno = request.POST['refno']

        

        roadfreight = RoadFreightShip.objects.filter(refno=currentrefno).values('owner')
        seafreight = SeaFreightShip.objects.filter(refno=currentrefno).values('owner')
        airfreight = AirFreightShip.objects.filter(refno=currentrefno).values('owner')
        # import pdb;pdb.set_trace()
        if len(roadfreight) > 0:
            currentowner = roadfreight[0]['owner']
        elif len(seafreight) > 0:
            currentowner = seafreight[0]['owner']
        elif len(airfreight) > 0:
            currentowner = airfreight[0]['owner']
        else:
            currentowner = "admin@ogl.com"

        email = EmailMessage(
            'Shipment Updated',
            'Dear Customer, There is a new update to your shipment. Kindly login to Navicus360 to view. Thank you.',
            settings.EMAIL_HOST_USER,
            [str(currentowner)]
        )

        email.fail_silently = True
        email.send()
        #return render(request,'index_fielduser.html',{'success':'success'})
        response = redirect('/keyuser')
        return response
        # return redirect(settings.BASEURL+"fielduser/")
    else:
        form = FreightForwarding()
        return render(request,"edit.html",{"form":form})