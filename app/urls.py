from django.urls import path
from django.conf.urls import url

from app.views import employee,department, plan_shift, shift_code, time_record, auth
from app.views.department import department_all
from . import views

app_name = 'time_attendance'

urlpatterns = [
  path('api/employees', employee.employee_all),
  url(r'^api/employees/department/([0-9]+)$', employee.employee_in_department),
  url(r'^api/employees/([0-9]+)$', employee.employee_info),

  path('api/departments/action', department.department_action),
  path('api/departments', department.department_all),
  url(r'^api/departments/([0-9]+)$', department.department_list),

  path('api/planshift', plan_shift.plan_all),
  path('api/planshift/action', plan_shift.plan_list),
  url(r'^api/planshift/action/([0-9]+)$', plan_shift.plan_list),      # for delete
  url(r'^api/planshift/department/([0-9]+)$', plan_shift.plan_department),
  url(r'^api/planshift/department/today/([0-9]+)$', plan_shift.plan_department_today),
  url(r'^api/planshift/employee/([0-9]+)$', plan_shift.plan_employee),
  url(r'^api/planshift/employee/today/([0-9]+)$', plan_shift.plan_employee_today),

  path('api/shiftcode', shift_code.all_shift_code),
  url(r'^api/shiftcode/(\d\d:\d\d:\d\d)$', shift_code.get_shift_code),
  
  path('api/timerecord', time_record.record_all),
  url(r'^api/timerecord/department/([0-9]+)$', time_record.record_department),
  path('api/timerecord/department/<int:depId>/<str:shift>', time_record.active_employee),
  url(r'^api/timerecord/employee/([0-9]+)$', time_record.record_employee),
  path('api/timerecord/new', time_record.manage_time_record),

  path('api/auth/login', auth.login_api),
  path('api/auth/logout', auth.logout_api),
  path('api/auth/getCurrentUserRole', auth.getCurrentUserRole)
]