from django.urls import path
from websiteapp1 import views

urlpatterns = [
    path('home/', views.home),
    path('page/', views.page),
    path('test/', views.test),
    path('test1/', views.test1)
]
