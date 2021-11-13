from django.db import models
from app.models.employee import *

class TimeRecord(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    emp = models.ManyToManyField('Employee', related_name='timerecords', blank=True)
    status = models.CharField(max_length=10)