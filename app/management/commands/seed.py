# <project>/<app>/management/commands/seed.py
from django.core.management.base import BaseCommand
import datetime

from app.models import Employee,Department,PlanShift,ShiftCode,TimeRecord, plan_shift

# Reading xls file for mock up
import xlrd

import datetime

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
  Department.objects.all().delete()
  PlanShift.objects.all().delete()
  ShiftCode.objects.all().delete()
  TimeRecord.objects.all().delete()

# Open mockup_data.xls
loc = ("Data_Table.xls")
workbook = xlrd.open_workbook(loc)

def create_employees():
  sheet = workbook.sheet_by_index(0)
  for i in range(1,sheet.nrows):
    data = sheet.row_values(i)
    department_list = str(data[4]).split(',')
    department_id = [int(x) for x in department_list if len(x)!=0]
    employee = Employee(
    name_title = data[1],
    first_name = data[2],
    last_name = data[3],
    hire_date = data[5],
    employee_type = data[6],
    role = data[7],
    email = data[8],
    password = data[9]
    )
    employee.save()
    employee.department.set(department_id)

  
def create_departments():
  sheet = workbook.sheet_by_index(1)
  for i in range(1,sheet.nrows):
    data = sheet.row_values(i)
    department = Department(
    dep_code = data[0],
    name = data[1],
    active_employee = data[2],
    total_employee = data[3],
    )
    department.save()

def convert_time(val):
  date_values = xlrd.xldate_as_tuple(val, workbook.datemode)
  time_value = datetime.time(*date_values[3:])
  return time_value

def convert_date(val):
  datetime_format = datetime.datetime(*xlrd.xldate_as_tuple(val, workbook.datemode))
  return datetime_format.strftime("%Y-%m-%d")

def create_timerecord():
  sheet = workbook.sheet_by_index(2)
  for i in range(1,sheet.nrows):
    data = sheet.row_values(i)
    employee_id = [int(data[3])]
    department_id = [int(data[1])]
    timerecord = TimeRecord(
    date = convert_date(data[0]),
    time = convert_time(data[2]),
    status = data[4],
    )
    timerecord.save()
    timerecord.employee.set(employee_id)
    timerecord.department.set(department_id)


def create_shiftcode():
  sheet = workbook.sheet_by_index(3)
  for i in range(1,sheet.nrows):
    data = sheet.row_values(i)
    shiftcode = ShiftCode(
    code = data[0],
    start_time = convert_time(data[1]),
    end_time = convert_time(data[2]),
    start_break = convert_time(data[3]),
    end_break = convert_time(data[4])
    )
    shiftcode.save()


def create_planshift():
  sheet = workbook.sheet_by_index(4)
  for i in range(1,sheet.nrows):
    data = sheet.row_values(i)
    employee_id = [int(data[2])]
    department_id = [int(data[1])]
    planshift = PlanShift(
    date = convert_date(data[0]),
    start_time = convert_time(data[3]),
    end_time = convert_time(data[4]),
    overtime = data[5]
    )
    planshift.save()
    planshift.employee.set(employee_id)
    planshift.department.set(department_id)

def run_seed(self, mode):
  """ Seed database based on mode
  :param mode: refresh / clear 
  :return:
  """
  # Clear data from tables
  # clear_data()
  if mode == MODE_CLEAR:
    return

  # Creating
  create_departments()   
  create_employees() 
  create_shiftcode()
  create_timerecord()  
  create_planshift()  
