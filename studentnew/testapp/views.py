from django.shortcuts import render
from testapp.models import Student

# Create your views here.
def home(request):
	return render(request,'testapp/homepage.html')

def student_info(request):
	students = Student.objects.all()
	return render(request,'testapp/studentinfo.html',{'students':students})
