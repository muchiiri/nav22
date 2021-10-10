from django.shortcuts import render,redirect
from .forms import *
from accounts.models import *
from django.contrib.auth.decorators import login_required,user_passes_test
from shipments.models import *
from django.conf import settings
import random
# Email Sending
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
import datetime
# Create your views here.

# Create your views here.
def not_in_oglstaff_group(user):
	if user.groups.filter(name='Ogl_fielduser').exists():
		return True
	else:
		return False

@login_required
@user_passes_test(not_in_oglstaff_group,login_url='/client/')
def home(request):
    roadfreight = RoadFreightShip.objects.filter(staff = request.user)
    seafreight = SeaFreightShip.objects.filter( staff= request.user)
    airfreight = AirFreightShip.objects.filter( staff= request.user)

    # shipmentstatus = FreightForwarding.objects.filter(shippingstatus = 'completed')
    # import pdb;pdb.set_trace()

    rno = len(roadfreight)
    sno = len(seafreight)
    airno = len(airfreight)
    allno = rno+sno+airno

    return render(request,"index_fielduser.html",{"group":"staff","context":roadfreight,"context2":seafreight,"context3":airfreight,"airno":airno,"sno":sno,"rno":rno,"allno":allno,"sidebar":"true"})

def home2(request):
    # roadfreight = RoadFreightShip.objects.all()
    roadfreight = RoadFreightShip.objects.filter( staff= request.user)
    seafreight = SeaFreightShip.objects.filter( staff= request.user)
    airfreight = AirFreightShip.objects.filter( staff= request.user)

    # shipmentstatus = FreightForwarding.objects.filter(shippingstatus = 'completed')
    # import pdb;pdb.set_trace()

    rno = len(roadfreight)
    sno = len(seafreight)
    airno = len(airfreight)
    allno = rno+sno+airno

    return render(request,"index_completed.html",{"group":"staff","context":roadfreight,"context2":seafreight,"context3":airfreight,"airno":airno,"sno":sno,"rno":rno,"allno":allno,"sidebar":"true"})

@login_required
def RoadFreightShip_view(request):
    context = {}
    #form = RoadFreightShipForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        form = RoadFreightShipForm(request.POST)
        # import pdb;pdb.set_trace()
        form = form.save(commit=False)
        print(request.user)
        # form.owner = request.POST.get("owner")
        form.staff = request.user
        form.save()
        print(form)

        currentowner = request.POST['owner']
        
        email = EmailMessage(
            'Road Freight Shipment created',
            'Dear Customer, A new Road freightship shipment has been created for you. Kindly login to Navicus360 system to view it. Thank you.',
            settings.EMAIL_HOST_USER,
            [str(currentowner)]
        )

        email.fail_silently = False
        email.send()
        response = redirect('/fielduser')
        return response
        
        # return render(request,"index_fielduser.html")
    else:
        print(request.user)
        roadform = RoadFreightShipForm()
        # roadform.getOwners()
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")
        lastone = year[-1]
        lasttwo = year[-2]
        
        n = random.randint(1000, 99999)
        refno = "OGLRF"+str(lasttwo)+str(lastone)+str(n)

        # get list of owners
        owners = []
        usergroup = Account.objects.filter(groups__name='Ogl Clients')
        usergrouplen = len(usergroup)
        for i in range(usergrouplen):
            owners.append(usergroup[i])

        form = RoadFreightShipForm()


    return render(request,"cargoroad.html",{'form':form,'group':'staff','refno':refno,"sidebar":"true","owners":owners})

@login_required
def AirFreightShip_view(request):
    context = {}
    #form = RoadFreightShipForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        form = AirFreightShipForm(request.POST)
        # import pdb;pdb.set_trace()
        form.shippingstatus = 'in-progress'
        form = form.save(commit=False)
        print(request.user)
        form.staff = request.user
        form.save()
        print(form)

        currentowner = request.POST['owner']
        
        email = EmailMessage(
            'Air Freight Shipment created',
            'Dear Customer, A new Air Freight shipment has been created for you. Kindly login to Navicus360 system to view it. Thank you.',
            settings.EMAIL_HOST_USER,
            [str(currentowner)]
        )

        email.fail_silently = False
        email.send()
        response = redirect('/fielduser')
        return response
        #return render(request,"index_fielduser.html")
    else:
        print(request.user)
        form = AirFreightShipForm()
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")
        lastone = year[-1]
        lasttwo = year[-2]
        
        n = random.randint(1000, 99999)
        refno = "OGLAF"+str(lasttwo)+str(lastone)+str(n)
        # get list of owners
        owners = []
        usergroup = Account.objects.filter(groups__name='Ogl Clients')
        usergrouplen = len(usergroup)
        for i in range(usergrouplen):
            owners.append(usergroup[i])

    return render(request,"cargoair.html",{'form':form,'group':'staff','refno':refno,"sidebar":"true","owners":owners})

@login_required
def SeaFreightShip_view(request):
    context = {}
    #form = RoadFreightShipForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        form = SeaFreightShipForm(request.POST)
        # import pdb;pdb.set_trace()
        form = form.save(commit=False)
        print(request.user)
        form.staff = request.user
        form.save()
        # print(form)

        currentowner = request.POST['owner']

        email = EmailMessage(
            'Sea Freight Shipment created',
            'Dear Customer, A new Sea Freight shipment has been created for you. Kindly login to Navicus360 system to view it. Thank you.',
            settings.EMAIL_HOST_USER,
            [str(currentowner)]
        )

        email.fail_silently = False
        email.send()

        response = redirect('/fielduser')
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
        form = SeaFreightShipForm()

        # get list of owners
        owners = []
        usergroup = Account.objects.filter(groups__name='Ogl Clients')
        usergrouplen = len(usergroup)
        for i in range(usergrouplen):
            owners.append(usergroup[i])

    return render(request,"cargosea.html",{'form':form,'group':'staff','refno':refno,"sidebar":"true","owners":owners})

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
        return redirect(settings.BASEURL+"fielduser/")

        #Edit Created Shipment
@login_required
def shipmentEdit(request, shipmentid, refno):
    roadForm = None
    if request.method == "GET" and refno[3] == 'R': 
        roadShipment = RoadFreightShip.object.get(id=shipmentid)
        roadForm = RoadFreightShipForm(instance=roadShipment)
    return render(request, 'shipmentedit.html', {'form': roadForm})


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
        return redirect(settings.BASEURL+"fielduser/")

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
        return redirect(settings.BASEURL+"fielduser/")


def view(request,uid,refno):
    userdetails_road = RoadFreightShip.objects.filter(id=uid)
    userdetails_sea = SeaFreightShip.objects.filter(id=uid)
    userdetails_air = AirFreightShip.objects.filter(id=uid)
    updateonshipments = FreightForwarding.objects.filter(refno=refno)
    return render(request,"view.html",{"context":userdetails_road,"context2":userdetails_sea,"context3":userdetails_air,"updateonshipments":updateonshipments,"group":"staff"})

def view2(request,uid,refno):
    #userdetails_road = RoadFreightShip.objects.filter(id=uid)
    userdetails_sea = SeaFreightShip.objects.filter(id=uid)
    #import pdb;pdb.set_trace()
    updateonshipments = FreightForwarding.objects.filter(refno=refno)
    return render(request,"view.html",{"context":userdetails_sea,"updateonshipments":updateonshipments,"group":"staff"})

def view3(request,uid,refno):
    #userdetails_road = RoadFreightShip.objects.filter(id=uid)
    userdetails_air = AirFreightShip.objects.filter(id=uid)
    #import pdb;pdb.set_trace()
    updateonshipments = FreightForwarding.objects.filter(refno=refno)
    return render(request,"view.html",{"context":userdetails_air,"updateonshipments":updateonshipments,"group":"staff"})

@login_required
def FreightForwardingView(request):
    if request.method == "POST":

        form = FreightForwarding()
        form.refno = request.POST.get("refno")
        refno_temp = request.POST.get("refno")
        
        form.etd = request.POST.get("etd")
        form.eta = request.POST.get("eta")
        form.sailingstatus = request.POST.get("sailingstatus")
        form.update = request.POST.get("update")
        form.staffcomments = request.POST.get("staffcomments")
        form.shippingstatus = request.POST.get("shippingstatus")
        form.save()
        

        currentrefno = request.POST['refno']
        #update on shipment creation models used by both keyuser and fielduser
        
        if currentrefno[3] == 'R':
            #get previous updates of this ref no;if eta or etd is blank use existing record
            if request.POST.get("etd") == "" and request.POST.get("eta") == "":
                prev_updates = RoadFreightShip.objects.get(refno = request.POST.get("refno"))
                prev_updates.current_etd = prev_updates.current_etd
                prev_updates.current_eta = prev_updates.current_eta
                prev_updates.current_sailingstatus =  request.POST.get("sailingstatus")
                prev_updates.shippingstatus = request.POST.get("shippingstatus")
                prev_updates.save()
            else:
                updates = RoadFreightShip.objects.get(refno = currentrefno)
                updates.current_etd =  request.POST.get("etd")
                updates.current_eta =  request.POST.get("eta")
                updates.current_sailingstatus =  request.POST.get("sailingstatus")
                updates.shippingstatus = request.POST.get("shippingstatus")
                updates.save()

        elif currentrefno[3] == 'S':
            #get previous updates of this ref no;if eta or etd is blank use existing record
            if request.POST.get("etd") == "" and request.POST.get("eta") == "":
                prev_updates = SeaFreightShip.objects.get(refno = currentrefno)
                prev_updates.current_etd = prev_updates.current_etd
                prev_updates.current_eta = prev_updates.current_eta
                prev_updates.current_sailingstatus =  request.POST.get("sailingstatus")
                prev_updates.shippingstatus = request.POST.get("shippingstatus")
                prev_updates.save()
            
            else:
                updates = SeaFreightShip.objects.get(refno = currentrefno)
                updates.current_etd =  request.POST.get("etd")
                updates.current_eta =  request.POST.get("eta")
                updates.current_sailingstatus =  request.POST.get("sailingstatus")
                updates.shippingstatus = request.POST.get("shippingstatus")
                updates.save()

        else:
            #get previous updates of this ref no;if eta or etd is blank use existing record
            if request.POST.get("etd") == "" and request.POST.get("eta") == "":
                prev_updates = AirFreightShip.objects.get(refno = currentrefno)
                prev_updates.current_etd = prev_updates.current_etd
                prev_updates.current_eta = prev_updates.current_eta
                prev_updates.current_sailingstatus =  request.POST.get("sailingstatus")
                prev_updates.shippingstatus = request.POST.get("shippingstatus")
                prev_updates.save()
            
            else:
                updates = AirFreightShip.objects.get(refno = currentrefno)
                updates.current_etd =  request.POST.get("etd")
                updates.current_eta =  request.POST.get("eta")
                updates.current_sailingstatus =  request.POST.get("sailingstatus")
                updates.shippingstatus = request.POST.get("shippingstatus")
                updates.save()

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

        # email = EmailMessage(
        #     'Shipment Updated',
        #     'Dear Customer, There is a new update to your shipment. Kindly login to Navicus360 to view. Thank you.',
        #     settings.EMAIL_HOST_USER,
        #     [str(currentowner)]
        # )

        # email.fail_silently = False
        # email.send()
        
        response = redirect('/fielduser')
        return response
        # return redirect(settings.BASEURL+"fielduser/")
    else:
        form = FreightForwarding()
        return render(request,"edit.html",{"form":form})

#Staff Notes updates
@login_required
def StaffFreightForwardingEdit(request):
    if request.method == "POST":
        form = StaffComments()
        form.remarks = request.POST.get("comments")
        currentrefno = request.POST['refno']
        form.save()

        return redirect(settings.BASEURL+"fielduser/")
    else:
        form = FreightForwarding()
        return render(request,"edit.html",{"form":form})
