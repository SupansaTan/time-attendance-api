from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view

from app.models import Employee
from app.serializers import EmployeeSerializer

@csrf_exempt
@api_view(['GET'])  #  /api/employees
def employee_list(request):
  if request.method == 'GET':
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return JsonResponse(serializer.data, safe=False)