from django.db import models
from app.models.employee import *

class Department(models.Model):
  parent_code = models.CharField(max_length=10,default='None')
  dep_code = models.CharField(max_length=10, default='None')
  name = models.CharField(max_length=100, default='None')
  active_employee = models.IntegerField(default=0)
  total_employee = models.IntegerField(default=0)
  manager = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='departments')