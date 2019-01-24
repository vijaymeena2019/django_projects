#from django.contrib import admin
from django.urls import path
from timeapp import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('datetime/', views.date_time),
    path('yourtime/', views.your_time),
]
