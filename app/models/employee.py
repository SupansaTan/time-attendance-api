from django.db import models
from app.models import Department

class Employee(models.Model):
  department = models.ForeignKey(Department, on_delete=models.CASCADE)
  name_title = models.CharField(max_length=6)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=100)
  hire_date = models.DateField(auto_now_add=True)
  employee_type = models.CharField(max_length=10)