from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from app.models import TimeRecord
from app.serializers import TimeRecordSerializer

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])

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
        record = TimeRecord.objects.get(id=record_data['id'])
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

