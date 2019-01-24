from django.contrib import admin
from testapp.models import Student


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
	list_display = ['stu_roll','stu_name','stu_fees','stu_city','stu_mobile','stu_dob','stu_email','stu_address']  

admin.site.register(Student,StudentAdmin)


VK7JG-NPHTM-C97JM-9MPGT-3V66T