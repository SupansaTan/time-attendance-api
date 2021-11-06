from django.db import models

class TimeRecord(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    emp_id = models.IntegerField()
    status = models.CharField(max_length=10)