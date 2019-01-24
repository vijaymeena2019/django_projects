from django.urls import path
from whatduration import views


urlpatterns = [
    path('timeduration/', views.time_duration),
    path('yourduration/', views.your_duration),
]
