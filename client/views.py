from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from shipments.models import *

from oglshipments.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import snoop
# from birdseye import eye
# import heartrate

# heartrate.trace(browser=True)
# @eye
def not_in_oglclients_group(user):
	if user.groups.filter(name='Ogl Clients').exists():
		return True
	else:
		return False



#DataFlair #Send Email
def sendmail(request):

    if request.method == 'GET':
        subject = 'Welcome OGL'
        message = 'You are now logged in'
        recepient = str("brykoech@gmail.com")
        #mail = send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
    #return mail

@login_required
#@user_passes_test(not_in_oglclients_group,login_url='/accounts/login')
# @eye
# @snoop
def home(request):
	
	usergroup = request.user.groups.values_list('name', flat=True).first()
	print(usergroup)
	currentuser = request.user

	if usergroup == "Ogl Clients":
		request.session['currentgroup'] = "client"
		road_list = RoadFreightShip.objects.filter(owner=currentuser)
		sea_list = SeaFreightShip.objects.filter(owner=currentuser)
		air_list = AirFreightShip.objects.filter(owner=currentuser)
		

		number_road = len(road_list)
		number_sea = len(sea_list)
		number_air = len(air_list)		
		return render(request,"index.html",{"context":road_list,"context2":sea_list,"context3":air_list,"rno":number_road,"sno":number_sea,"airno":number_air})

	elif usergroup == "Ogl_fielduser":
		request.session['currentgroup'] = "fielduser"
		return redirect("/fielduser/")

	elif usergroup == "Ogl_keyuser":
		request.session['currentgroup'] = "keyuser"
		return redirect("/keyuser/")

	else:
		request.session['currentgroup'] = "client"
		return render(request,"index.html")

def homecomplete(request):
	#sendmail(request)
	usergroup = request.user.groups.values_list('name', flat=True).first()
	print(usergroup)
	#import pdb;pdb.set_trace()
	if usergroup == "Ogl Clients":
		currentuser = request.user
		road_list = RoadFreightShip.objects.filter(owner=currentuser)
		sea_list = SeaFreightShip.objects.filter(owner=currentuser)
		air_list = AirFreightShip.objects.filter(owner=currentuser)
		# import pdb;pdb.set_trace()
		# allfreightformward = FreightForwarding.objects.all()
		

		number_road = len(road_list)
		number_sea = len(sea_list)
		number_air = len(air_list)		
		
		return render(request,"index_complete.html",{"context":road_list,"context2":sea_list,"context3":air_list,"rno":number_road,"sno":number_sea,"airno":number_air})
	# elif usergroup == "Ogl_fielduser":
	# 	#return render(request,"index_fielduser.html")
	# 	return redirect("/fielduser/")
	# elif usergroup == "Ogl_keyuser":
	# 	# return redirect("/keyuser/") original, changed to line below
	# 	return redirect("/fielduser/")
	# else:
	# 	return render(request,"index.html")

def view(request,uid,refno):
	userdetails_r = RoadFreightShip.objects.filter(id=uid)
	userdetails_sea = SeaFreightShip.objects.filter(id=uid)
	updateonshipments = FreightForwarding.objects.filter(refno=refno)
	return render(request,"view.html",{"context":userdetails_r,"updateonshipments":updateonshipments,"group":"client"})

def view2(request,uid,refno):
	userdetails_sea = SeaFreightShip.objects.filter(id=uid)
	updateonshipments = FreightForwarding.objects.filter(refno=refno)
	return render(request,"view.html",{"context":userdetails_sea,"updateonshipments":updateonshipments,"group":"client"})

def view3(request,uid,refno):
	userdetails_air = AirFreightShip.objects.filter(id=uid)
	updateonshipments = FreightForwarding.objects.filter(refno=refno)
	return render(request,"view.html",{"context":userdetails_air,"updateonshipments":updateonshipments,"group":"client"})