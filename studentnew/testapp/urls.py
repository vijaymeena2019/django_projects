from django.urls import path
from testapp import views

urlpatterns = [
	path('home/', views.home),
	path('studentinfo/', views.student_info)
]