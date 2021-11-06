from django.db import models

class Department(models.Model):
  parent_code = models.CharField(max_length=10,default='None')
  dep_code = models.CharField(max_length=10, default='None')
  name = models.CharField(max_length=100, default='None')
  active_employee = models.IntegerField(default=0)
  total_employee = models.IntegerField(default=0)
  manager_id = models.IntegerField(default=0)