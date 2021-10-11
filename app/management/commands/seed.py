# <project>/<app>/management/commands/seed.py
from django.core.management.base import BaseCommand
import datetime

from app.models import Employee

# python manage.py seed --mode=refresh
""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'

class Command(BaseCommand):
  help = "seed database for testing and development."

  def add_arguments(self, parser):
    parser.add_argument('--mode', type=str, help="Mode")

  def handle(self, *args, **options):
    self.stdout.write('seeding data...')
    run_seed(self, options['mode'])
    self.stdout.write('done.')

def clear_data():
  """Deletes all the table data"""
  Employee.objects.all().delete()

def create_employees():
  mock_employees = [
    {
      'name_title': 'นาย',
      'first_name': 'ภูสิทธิ',
      'last_name': 'บาดตาสาว',
      'hire_date': datetime.datetime(2018, 6, 1),
      'employee_type': 'monthly'
    },
    {
      'name_title': 'นางสาว',
      'first_name': 'นฤมล',
      'last_name': 'มนูญศักดิ์',
      'hire_date': datetime.datetime(2019, 1, 1),
      'employee_type': 'monthly'
    },
    {
      'name_title': 'นาย',
      'first_name': 'ไกรยุทธ์',
      'last_name': 'อัศวรัช',
      'hire_date': datetime.datetime(2020, 2, 9),
      'employee_type': 'daily'
    }
  ]

  for i in range(len(mock_employees)):
    employee = Employee(
      name_title = mock_employees[i]['name_title'],
      first_name = mock_employees[i]['first_name'],
      last_name = mock_employees[i]['last_name'],
      hire_date = mock_employees[i]['hire_date'],
      employee_type = mock_employees[i]['employee_type']
    )
    employee.save()

def run_seed(self, mode):
  """ Seed database based on mode
  :param mode: refresh / clear 
  :return:
  """
  # Clear data from tables
  clear_data()
  if mode == MODE_CLEAR:
    return

  # Creating employees
  create_employees()