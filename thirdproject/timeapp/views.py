from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def date_time(request):
    return HttpResponse('<h1>The time is L: '+str(datetime.datetime.now())+'</h1>')

def your_time(request):
    return HttpResponse('<h1>Your time is going fine and do fight to do more</h1>')
