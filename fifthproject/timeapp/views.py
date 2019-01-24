from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def time_server(request):
    #time= datetime.datetime.now()
    return render(request,'timeapp/timeapp_results.html',{'samay':datetime.datetime.now()})

def your_time(request):
    return HttpResponse('<h1> Your time is going good </h1>')
