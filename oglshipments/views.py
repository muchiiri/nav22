from django.shortcuts import render,redirect
from accounts.models import Account

def Home(request):
    return render(request,"Home.html")

def profileView(request):
    # currentuser = request.user
    # userinfo = Account()
    baseurl = request.get_full_path()

    return render(request,"profile.html",{"baseurl":baseurl})