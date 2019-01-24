from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def date_time_server(request):
    return HttpResponse('<h1>The Date and Time of Server is '+ str(datetime.datetime.now()) +'</h1>')
