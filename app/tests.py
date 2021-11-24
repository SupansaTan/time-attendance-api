
from django.test import TestCase, Client

from .models import Employee, Department, ShiftCode, TimeRecord, PlanShift
from .serializers import EmployeeSerializer, DepartmentSerializer, TimeRecordSerializer, PlanShiftSerializer
from rest_framework import status
from django.contrib.auth.models import User
import json


# initialize the APIClient app
client = Client()

""" Test module for Employee model """
class EmployeeTest(TestCase):
    """mock up data"""
    def setUp(self):
        self.empA = Employee.objects.create(
            name_title = 'นาย', 
            first_name = 'กระต่าย', 
            last_name = 'กระรอก', 
            employee_type = 'monthly',
            role = 'manager',
            user = User.objects.create(username='yyy', first_name='xxx', last_name='zzz'),
        )
        self.empB = Employee.objects.create(
            name_title = 'นาย', 
            first_name = 'ฉลาม', 
            last_name = 'เรือใบ', 
            employee_type = 'daily',
            role = 'employee',
            user = User.objects.create(username='aaa', first_name='bbb', last_name='ccc'),
        )

    def test_get_all_employee(self):
        # get API response
        response = self.client.get("/api/employees")
        # get data from db
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_employee(self):
        response = client.get("http://127.0.0.1:8000/api/employees/" + str(self.empA.id))
        employee = Employee.objects.filter(id=self.empA.id)
        serializer = EmployeeSerializer(employee, many=True)
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # invalid get
    def test_get_invalid_single_employee(self):
        response = client.get("http://127.0.0.1:8000/api/employees/"+ "A")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)



""" Test module for Department model """
class DepartmentTest(TestCase):

    def setUp(self):
        self.depA = Department.objects.create(
            dep_code = 'A001', 
            name = 'เชือดไก่ 1', 
            active_employee = 0, 
            total_employee = 17,
        )
        self.dpeB = Department.objects.create(
            dep_code = 'A002', 
            name = 'เชือดไก่ 2', 
            active_employee = 0, 
            total_employee = 15,
        )

    def test_get_all_department(self):
        # get API response
        response = self.client.get("/api/departments")
        # get data from db
        department = Department.objects.all()
        serializer = DepartmentSerializer(department, many=True)
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)




""" Test module for TimeRecord model """
class TimeRecordTest(TestCase):

    def setUp(self):
        self.empA = Employee.objects.create(
            name_title = 'นาย', 
            first_name = 'กระต่าย', 
            last_name = 'กระรอก', 
            employee_type = 'monthly',
            role = 'employee',
            user =  User.objects.create(username='yyy', first_name='xxx', last_name='zzz'),
        )
        self.depA = Department.objects.create(
            dep_code = 'A001', 
            name = 'เชือดไก่ 1', 
            active_employee = 0, 
            total_employee = 17,
        )
        self.recordA = TimeRecord.objects.create(
            status = "In",
        )
        self.recordA.employee.set([self.empA.id])
        self.recordA.department.set([self.depA.id])

    def test_get_all_time_record(self):
         # get API response
        response = self.client.get("/api/timerecord")
        # get data from db
        timerecord = TimeRecord.objects.all()
        serializer = TimeRecordSerializer(timerecord, many=True)
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)




""" Test module for PlanShift model """
class PlanshiftTest(TestCase):

    def setUp(self):
        self.empA = Employee.objects.create(
            name_title = 'นาย', 
            first_name = 'กระต่าย', 
            last_name = 'กระรอก', 
            employee_type = 'monthly',
            role = 'employee',
            user = User.objects.create(username='yyy', first_name='xxx', last_name='zzz'),
        )
        self.depA = Department.objects.create(
            dep_code = 'A001', 
            name = 'เชือดไก่ 1', 
            active_employee = 0, 
            total_employee = 17,
        )
        self.planA = PlanShift.objects.create(
            date = '2021-11-20', 
            start_time = '00:00:00',
            end_time = '09:00:00', 
            overtime = 0,
        )
        self.planA.employee.set([self.empA.id])
        self.planA.department.set([self.depA.id])

        ShiftCode.objects.create(
            code = "01H00-10H00",
            start_time = "01:00:00",
            end_time = "10:00:00",
            start_break = "05:00:00",
            end_break = "06:00:00",
            )

        # for add planshift
        self.payload = {
            'department': [self.depA.id],
            'employee_list': [self.empA.id],
            'start_date': "2021-11-17",
            'end_date':"2021-11-17"
        }

    def test_get_all_planshift(self):
        # get API response
        response = self.client.get("/api/planshift")
        # get data from db
        planshift = PlanShift.objects.all()
        serializer = PlanShiftSerializer(planshift, many=True)
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # add just shift time
    def test_add_plan_shift(self):
        self.payload["start_time"] = "01:00:00" 
        response = client.post("http://127.0.0.1:8000/api/planshift/action",
            data=json.dumps(self.payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), "Add Successfully.")

    # add just OT
    def test_add_plan_ot(self):
        self.payload["overtime"] = 1 
        response = client.post("http://127.0.0.1:8000/api/planshift/action",
            data=json.dumps(self.payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), "Add Successfully.")

    # add both shift time and OT
    def test_add_plan_shift_ot(self):
        self.payload["start_time"] = "01:00:00" 
        self.payload["overtime"] = 1 
        response = client.post("http://127.0.0.1:8000/api/planshift/action",
            data=json.dumps(self.payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), "Add Successfully.")

    # delete planshift
    def test_delete_plan(self):
        response = client.delete( "http://127.0.0.1:8000/api/planshift/action/"+ str(self.empA.id) )
        self.assertEqual(response.json(), "Delete Successfully.")