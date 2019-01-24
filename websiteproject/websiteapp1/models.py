from django.db import models

# Create your models here.
class Employee(models.Model): #creating child class of Model class ClassName(object)

    eno = models.IntegerField()
    esal = models.FloatField()
    eaddr = models.CharField(max_length = 64)
    ename = models.CharField(max_length = 64)
