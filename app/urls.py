from django.urls import path

from . import views

app_name = 'time_attendance'

urlpatterns = [
  path('api/employees', views.employee_list)
]