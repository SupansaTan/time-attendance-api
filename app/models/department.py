from django.db import models
from app.models.employee import *

class Department(models.Model):
  dep_code = models.CharField(max_length=10, default='')
  name = models.CharField(max_length=100, default='')
  active_employee = models.IntegerField(default=0)
  total_employee = models.IntegerField(default=0)