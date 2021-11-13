from django.urls import path
from django.conf.urls import url

from app.views import employee,department, plan_shift, shift_code, time_record
from . import views

app_name = 'time_attendance'

urlpatterns = [
  path('api/employees', employee.employee_all),
  url(r'^api/employees/([0-9]+)$', employee.employee_list),
  url(r'^api/dashboard/([0-9]+)$', employee.employee_info),

  path('api/departments', department.department_all),
  url(r'^api/departments/([0-9]+)$', department.department_list),

  path('api/planshift', plan_shift.plan_all),
  url(r'^api/planshift/([0-9]+)$', plan_shift.plan_department),

  path('api/shiftcode', shift_code.all_shift_code),
  
  path('api/timerecord', time_record.record_all),
  url(r'^api/timerecord/([0-9]+)$', time_record.record_department)
]