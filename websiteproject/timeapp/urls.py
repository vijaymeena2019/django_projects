from django.urls import path
from timeapp import views

urlpatterns = [
    path('time/', views.time),
    path('test/', views.test)
]
