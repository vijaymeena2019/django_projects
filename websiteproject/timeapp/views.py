from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def time(request):
    time = datetime.datetime.now()
    return render(request,'timeapp/results.html',{'time':time})

def test(request):
    return HttpResponse('<h1> the test of time app is proper</h1>')
