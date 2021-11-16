from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response

from app.models import PlanShift, employee
from app.serializers import PlanShiftSerializer

from django.db.models import Q

import datetime

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])

# GET plan data from employee id

def plan_list(request):
    if request.method == 'GET':
        planshift = PlanShift.objects.all()
        serializer = PlanShiftSerializer(planshift, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        planshift_data = JSONParser().parse(request)
        serializer = PlanShiftSerializer(data=planshift_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Add Successfully.", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        planshift_data = JSONParser().parse(request)
        planshift = PlanShift.objects.get(id=planshift_data['id'])
        serializer = PlanShiftSerializer(planshift,data=planshift_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Update Successfully.", safe=False)
        return JsonResponse("Failed to update.", safe=False)

    elif request.method == 'DELETE':
        planshift_data = JSONParser().parse(request)
        planshift = PlanShift.objects.get(id=planshift_data['id'])
        planshift.delete()
        return JsonResponse("Delete Successfully.", safe=False)


# GET plan data by employee id from date today++ 
def plan_employee(request,val):
    if request.method == 'GET':
        today = datetime.datetime.today()
        planshift = PlanShift.objects.filter(employee=val).filter(Q(date__gte=today)|Q(date=None))

        serializer = PlanShiftSerializer(planshift, many=True)
        return JsonResponse(serializer.data, safe=False)

def plan_employee_today(request,val):
    if request.method == 'GET':
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        planshift = PlanShift.objects.filter(employee=val, date=today)
        serializer = PlanShiftSerializer(planshift, many=True)
        return JsonResponse(serializer.data, safe=False)

# GET plan data from department id
def plan_department(request,val):
    if request.method == 'GET':
        planshift = PlanShift.objects.filter(department=val)
        serializer = PlanShiftSerializer(planshift, many=True)
        return JsonResponse(serializer.data, safe=False)

def plan_department_today(request,val):
    if request.method == 'GET':
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        planshift = PlanShift.objects.filter(department=val, date=today)
        serializer = PlanShiftSerializer(planshift, many=True)
        return JsonResponse(serializer.data, safe=False)

def plan_all(request):
    if request.method == 'GET':
        planshift = PlanShift.objects.all()
        serializer = PlanShiftSerializer(planshift, many=True)
        return JsonResponse(serializer.data, safe=False)