from django.db import models
from app.models.employee import *

class PlanShift(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    dep_code = models.CharField(max_length=10)
    emp = models.ManyToManyField('Employee', related_name='planshifts', blank=True)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    overtime = models.IntegerField()