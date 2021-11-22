from django.db import models
from app.models.employee import *

class PlanShift(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    department = models.ManyToManyField('Department', related_name='dep_plan', blank=True)
    employee = models.ManyToManyField('Employee', related_name='emp_plan', blank=True)
    start_time = models.TimeField(auto_now=False, auto_now_add=False, blank=True, default="00:00:00")
    end_time = models.TimeField(auto_now=False, auto_now_add=False, blank=True, default="00:00:00")
    overtime = models.IntegerField(blank=True, default=0)