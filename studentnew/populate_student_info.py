import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','studentnew.settings')
django.setup()

from faker import Faker 
from random import randint
from testapp.models import Student

#   stu_roll = models.IntegerField()
# 	stu_name = models.CharField(max_length = 30)
# 	stu_city = models.CharField(max_length = 30)
# 	stu_fees = models.FloatField()
# 	stu_mobile = models.IntegerField()
# 	stu_address = models.TextField()
# 	stu_dob = models.DateField()
# 	stu_email = models.EmailField()
	


fake = Faker()

def indian_mobile():
	no=str(randint(7,9))
	for i in range(9):
		no+=str(randint(0,9))
	return int(no)

def populate(n):
	for i in range(n):
		froll = fake.random_int(min=1,max=999)
		fcity = fake.city()
		fdob = fake.date()
		ffees = fake.random_int(min=1000,max=9999)
		#fmobile = indian_mobile()
		fmobile = fake.random_int(min=7000000,max=9999999)
		fadd = fake.address()
		femail = fake.email()
		fname = fake.name()

		student_record=Student.objects.get_or_create(stu_roll=froll,stu_name=fname,stu_dob=fdob,stu_address=fadd,stu_fees=ffees,stu_mobile=fmobile,stu_city=fcity,stu_email=femail)

getn = int(input('please enter how many number of fake data you want?'))

populate(getn)


