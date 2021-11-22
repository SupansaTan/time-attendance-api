from django.db import models
from app.models.department import *
from django.contrib.auth.models import User

class Employee(models.Model):
  id = models.AutoField(primary_key=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
  name_title = models.CharField(max_length=6,default='')
  first_name = models.CharField(max_length=50,default='')
  last_name = models.CharField(max_length=50,default='')
  department = models.ManyToManyField('Department', related_name='employees', blank=True)
  hire_date = models.DateField(auto_now_add=True)
  employee_type = models.CharField(max_length=10,default='m')
  role = models.CharField(max_length=10,default='employee')
  email = models.CharField(max_length=50, default='')
  password = models.CharField(max_length=50,default='')