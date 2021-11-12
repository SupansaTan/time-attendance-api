from django.urls import path

from app.views import department, plan_shift, shift_code, time_record
from . import views

app_name = 'time_attendance'

urlpatterns = [
  path('api/employees', views.employee_all),
  path('api/departments', department.department_all),
  path('api/planshift', plan_shift.plan_all),
  path(r'^api/planshift/([0-9]+)$', plan_shift.plan_department),
  path('api/shiftcode', shift_code.all_shift_code),
  path('api/timerecord', time_record.record_all),
]