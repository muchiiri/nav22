from django.shortcuts import render,redirect
from django.template import RequestContext
from accounts.models import Account

def Home(request):
    baseurl = request.get_full_path()
    return render(request,"Home.html", {"baseurl":baseurl})

def profileView(request):
    # currentuser = request.user
    # userinfo = Account()
    baseurl = request.get_full_path()

    return render(request,"profile.html",{"baseurl":baseurl})

#Custom errors pages
def handler404(request, exception):
    response = render(request,"error404.html", status=404)