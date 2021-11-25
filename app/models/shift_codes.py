from django.db import models

class ShiftCode(models.Model):
    code = models.SlugField()
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    start_break = models.TimeField(auto_now=False, auto_now_add=False)
    end_break = models.TimeField(auto_now=False, auto_now_add=False)