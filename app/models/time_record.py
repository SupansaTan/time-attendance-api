from django.db import models
from app.models.employee import *

class TimeRecord(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    emp = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='time_records')
    status = models.CharField(max_length=10)