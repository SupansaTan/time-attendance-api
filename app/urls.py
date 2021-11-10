from django.urls import path

from app.views import department, plan_shift, shift_code, time_record
from . import views

app_name = 'time_attendance'

urlpatterns = [
  path('api/employees', views.employee_list),
  path('api/departments', department.department_list),
  path('api/planshift', plan_shift.plan_list),
  path('api/shiftcode', shift_code.shift_code),
  path('api/timerecord', time_record.time_record),
]