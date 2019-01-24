from django.shortcuts import render
from django.http import HttpResponse
from websiteapp1.models import Employee
import datetime

# Create your views here.
def home(request):
    return render(request,'websiteapp1/results.html',{'name':'vijay'})

def page(request):
    time= datetime.datetime.now()
    return render(request,'timeapp/results.html',{'time':time})

def test(request):
    return HttpResponse('<h1>test response is sucessful</h1>')

def test1(request):
    employees = Employee.objects.all()
    return render(request,"websiteapp1/results2.html",{'employees':employees})
