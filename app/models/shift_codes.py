from django.db import models

class ShiftCode(models.Model):
    code = models.CharField(max_length=15)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    start_break = models.TimeField(auto_now=False, auto_now_add=False)
    end_break = models.TimeField(auto_now=False, auto_now_add=False)