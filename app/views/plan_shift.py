from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from app.models import PlanShift
from app.serializers import PlanShiftSerializer

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])

def plan_list(request,param=0):
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