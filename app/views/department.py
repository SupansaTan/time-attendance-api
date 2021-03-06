from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

from app.models import Department
from app.serializers import DepartmentSerializer

@csrf_exempt
@api_view(['GET', 'POST','PUT','DELETE'])
@permission_classes([AllowAny])
# GET departments data from department id

def department_action(request):
    if request.method == 'GET':
        department = Department.objects.all()
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
        department = Department.objects.get(dep_code=department_data['dep_code'])
        department.delete()
        return JsonResponse("Delete Successfully.", safe=False)

def department_all(request):
    if request.method == 'GET':
        department = Department.objects.all()
        serializer = DepartmentSerializer(department, many=True)
        return JsonResponse(serializer.data, safe=False)

def department_list(request,val):
    if request.method == 'GET':
        department = Department.objects.filter(id=val)
        serializer = DepartmentSerializer(department, many=True)
        return JsonResponse(serializer.data, safe=False)
