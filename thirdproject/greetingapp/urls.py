#from django.contrib import admin
from django.urls import path
from greetingapp import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('diwali/', views.diwali_greeting_view),
    path('happy/', views.holi_greeding_view),
    path('birthday/', views.birthday_greeting_view),
]
