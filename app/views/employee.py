from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from app.models import Employee
from app.serializers import EmployeeSerializer

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
# GET employees from department id

def employee_list(request,val):
  if request.method == 'GET':
    employee = Employee.objects.filter(department=val)
    serializer = EmployeeSerializer(employee, many=True)
    return JsonResponse(serializer.data, safe=False)

  elif request.method == 'POST':
    employee_data = JSONParser().parse(request)
    serializer = EmployeeSerializer(data=employee_data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse("Add Successfully.", safe=False)
    return JsonResponse("Failed to add.", safe=False)

  elif request.method == 'PUT':
    employee_data = JSONParser().parse(request)
    employee = Employee.objects.get(id=employee_data['id'])
    serializer = EmployeeSerializer(employee,data=employee_data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse("Update Successfully.", safe=False)
    return JsonResponse("Failed to Update.", safe=False)

  elif request.method == 'DELETE':
    employee_data = JSONParser().parse(request)
    employee = Employee.objects.get(id=employee_data['id'])
    employee.delete()
    return JsonResponse("Delete Successfully.", safe=False)

def employee_all(request):
  if request.method == 'GET':
    employee = Employee.objects.all()
    serializer = EmployeeSerializer(employee, many=True)
    return JsonResponse(serializer.data, safe=False)

def employee_info(request,val):
  if request.method == 'GET':
    employee = Employee.objects.filter(id=val)
    serializer = EmployeeSerializer(employee, many=True)
    return JsonResponse(serializer.data, safe=False)

def employee_in_department(request,val):
  if request.method == 'GET':
    employee = Employee.objects.filter(department=val , role='employee')
    serializer = EmployeeSerializer(employee, many=True)
    return JsonResponse(serializer.data, safe=False)