from django.contrib import admin
from websiteapp1.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    display_list = ['eno','ename']

admin.site.register(Employee,EmployeeAdmin)

# def EmployeeAdmin(models.ModelAdmin)
