from django.db import models
from app.models.employee import *

class TimeRecord(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    department = models.ManyToManyField('Department', related_name='dep_records')
    employee = models.ManyToManyField('Employee', related_name='emp_records')
    status = models.CharField(max_length=10)