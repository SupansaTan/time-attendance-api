from django.db import models
from app.models.department import *

class Employee(models.Model):
  employee_id = models.AutoField(primary_key=True)
  name_title = models.CharField(max_length=6,default='None')
  first_name = models.CharField(max_length=50,default='None')
  last_name = models.CharField(max_length=50,default='None')
  department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='employees')
  hire_date = models.DateField(auto_now=False, auto_now_add=False)
  employee_type = models.CharField(max_length=10,default='None')
  role = models.CharField(max_length=10,default='None')
  email = models.CharField(max_length=50,default='None')
  password = models.CharField(max_length=50,default='None')