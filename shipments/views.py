from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from shipments.models import *
from django.conf import settings
import random
# Create your views here.

@login_required
def editRoadFreigh(request,userid):
    #userid = userid
    if request.method == "GET":
        RoadModelobject = RoadFreightShip.objects.get(id=userid)
        return render(request,'edit.html',{'roadfreigh':RoadModelobject})   
    else:
        #print(userid)
        #import pdb;pdb.set_trace()
        form = FreightForwarding(request.POST)
        form = form.save(commit=False)

        #refno = request.POST.get("refno")
        #form.refno = refno
        form.save()
        #form = (request.POST)
        # owner = request.POST.get("owner")
        # country = request.POST.get("country")
        # town = request.POST.get("town")
        # form.cargo_description = request.POST.get("desc")
        # form.placeofloading = request.POST.get("load")
        # form.placeofdelivery = request.POST.get("delivery")
        # form.cargoload = request.POST.get("cload")
        
        

        #return render(request,'index_fielduser.html',{'success':'success'})
        return redirect(settings.BASEURL+"fielduser/")
