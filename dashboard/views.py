from django.shortcuts import render
from django.views.generic import View
from django.conf import settings
from quote.models import *
from django.http import HttpResponse
from accounts.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import pdb

class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):

        #Recent Quotes
        currentuser = request.session['currentuser']
        recentquotes = Quote_App.objects.filter(owner=currentuser) [:5]
        '''
            HomeView class is handling the rendering of the template,
            it makes a call to the ChartData view to get the data and it passes the data as a context variable
            to the render function. 
            It also extracts the value of quotes_road, quotes_sea, quotes_air, and quotes_warehouse from the returned data
            and pass it along as a context variable to the template.
            The ChartData class remains mostly the same, but it's only responsible for providing the data in json format.
        '''
        chart_data = ChartData().get(request).data
        quotes_air = chart_data.get('chartdata')[0]
        quotes_sea = chart_data.get('chartdata')[1]
        quotes_road = chart_data.get('chartdata')[2]
        quotes_warehouse = chart_data.get('chartdata')[3]

        context = {
            'chart_data': chart_data,
            'quotes_air': quotes_air,
            'quotes_sea': quotes_sea,
            'quotes_road': quotes_road,
            'quotes_warehouse': quotes_warehouse,
            'recentquotes': recentquotes
        }

        return render(request, 'dashboard.html', context)


class ChartData(APIView):
    
    authentication_classes = []
    permission_classes = []
    
    def get(self, request, format = None):
        #current user
        # pdb.set_trace()
        currentuser = request.session['currentuser']
        # print(currentuser)
        quotes_air = Quote_App.objects.filter(owner=currentuser, quote_type='Air').count()
        quotes_air = int(quotes_air)
        # print('Air Quotes:', quotes_air)

        quotes_road = Quote_App.objects.filter(owner=currentuser, quote_type='Road').count()
        # quotes_road = Quote_Road.objects.filter(count()
        quotes_road = int(quotes_road)
        # print('Road Quotes:', quotes_road)

        quotes_sea = Quote_App.objects.filter(quote_type='Sea').count()
        quotes_sea = int(quotes_sea)
        # print('Sea Quotes:', quotes_sea)

        quotes_warehouse = Quote_App.objects.filter(owner=currentuser, quote_type='Warehouse').count()
        quotes_warehouse = int(quotes_warehouse)
        # print('Warehouse Quotes:', quotes_warehouse)

        # Convert into list
        chartLabel = "Quotes"
        labels = ['Air', 'Sea', 'Road', 'Warehouse']
        chartdata = [quotes_air, quotes_sea, quotes_road, quotes_warehouse]
        # chartdata = [20, 30, 10, 18]

        #convert the lists into a dictionary
        data = {
            'chartLabel': chartLabel,
            'labels' : labels,
            'chartdata' : chartdata
            }
        # pdb.set_trace()
        
        return Response(data)