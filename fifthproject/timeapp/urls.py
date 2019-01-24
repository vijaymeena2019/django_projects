from django.urls import path
from timeapp import views


urlpatterns = [
    path('time/', views.time_server),
    path('yourtime/', views.your_time)
]
