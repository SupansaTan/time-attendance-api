from django.db import models

class PlanShift(models.Model):
    date = models.DateField(auto_now_add=True)
    dep_code = models.CharField(max_length=10)
    emp_id = models.IntegerField()
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    overtime = models.IntegerField()