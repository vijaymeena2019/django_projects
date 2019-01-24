from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def birthday_greeting_view(request):
    return HttpResponse('<h1>Happy Birthday Greeting From Vijay Meena</h1>')

def diwali_greeting_view(request):
    return HttpResponse('<h1>Happy Diwali greeting from vijay meena')

def holi_greeding_view(request):
    return HttpResponse('<h1>Happy Holi greeting from vijay meena')
