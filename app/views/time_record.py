from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from app.models import TimeRecord, ShiftCode
from app.serializers import TimeRecordSerializer

import datetime
from datetime import timedelta

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
# GET time record data from id

def time_record(request):
    if request.method == 'GET':
        record = TimeRecord.objects.all()
        serializer = TimeRecordSerializer(record, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        record_data = JSONParser().parse(request)
        serializer = TimeRecordSerializer(data=record_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Add Successfully.", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        record_data = JSONParser().parse(request)
        record = TimeRecord.objects.get(department=record_data['department'][0],employee=record_data['employee'][0])
        serializer = TimeRecordSerializer(record,data=record_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Update Successfully.", safe=False)
        return JsonResponse("Failed to update.", safe=False)

    elif request.method == 'DELETE':
        record_data = JSONParser().parse(request)
        record = TimeRecord.objects.get(id=record_data['id'])
        record.delete()
        return JsonResponse("Delete Successfully.", safe=False)

def record_all(request):
    if request.method == 'GET':
        record = TimeRecord.objects.all()
        serializer = TimeRecordSerializer(record, many=True)
        return JsonResponse(serializer.data, safe=False)


# GET today time record from department id
def record_department(request,val):
    if request.method == 'GET':
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        record = TimeRecord.objects.filter(department=val, date=today)
        serializer = TimeRecordSerializer(record, many=True)
        return JsonResponse(serializer.data, safe=False)

# GET active employee on that shift from department id and shift
def active_employee(request, depId, shift):
    if request.method == 'GET':
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        before_start = (datetime.datetime.strptime(shift, '%H:%M:%S') - timedelta(minutes=30)).time() # get to work half an hour early.
        end_time = ShiftCode.objects.get(start_time=shift).end_time
        record = TimeRecord.objects.filter(department=depId, date=today, status='In', time__gte=before_start, time__lte=end_time)
        serializer = TimeRecordSerializer(record, many=True)
        return JsonResponse(serializer.data, safe=False)
    
# GET today time record from department id
def record_employee(request,val):
    if request.method == 'GET':
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        record = TimeRecord.objects.filter(employee=val, date=today)
        serializer = TimeRecordSerializer(record, many=True)
        return JsonResponse(serializer.data, safe=False)

