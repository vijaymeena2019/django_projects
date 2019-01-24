from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello_world_view(request): #all takes argument from server
        return HttpResponse('<h1> Hello This is response from django application created by vijay meena </h1>')
