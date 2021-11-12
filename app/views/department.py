from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from app.models import Department
from app.serializers import DepartmentSerializer

@csrf_exempt
@api_view(['GET', 'POST','PUT','DELETE'])

# GET departments data from department id

def department_list(request,param=0):
    if request.method == 'GET':
        department_data = JSONParser().parse(request)
        department_id = department_data['id']
        department = Department.objects.filter(id=department_id)
        serializer = DepartmentSerializer(department, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        serializer = DepartmentSerializer(data=department_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Add Successfully.", safe=False)
        return JsonResponse("Failed to add.", safe=False)

    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Department.objects.get(id=department_data['id'])
        serializer = DepartmentSerializer(department,data=department_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Update Successfully.", safe=False)
        return JsonResponse("Failed to update.", safe=False)

    elif request.method == 'DELETE':
        department_data = JSONParser().parse(request)
        department = Department.objects.get(id=department_data['id'])
        department.delete()
        return JsonResponse("Delete Successfully.", safe=False)

def department_all(request):
    if request.method == 'GET':
        department = Department.objects.all()
        serializer = DepartmentSerializer(department, many=True)
        return JsonResponse(serializer.data, safe=False)
