from django.db import models

# Create your models here.
class Student(models.Model):
	stu_roll = models.IntegerField()
	stu_name = models.CharField(max_length = 30)
	stu_city = models.CharField(max_length = 30)
	stu_fees = models.FloatField()
	stu_mobile = models.IntegerField()
	stu_address = models.TextField()
	stu_dob = models.DateField()
	stu_email = models.EmailField()



