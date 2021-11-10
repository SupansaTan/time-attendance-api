from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

from app.models import ShiftCode
from app.serializers import ShiftCodeSerializer

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])

def shift_code(request):
  if request.method == 'GET':
    shiftcode = ShiftCode.objects.all()
    serializer = ShiftCodeSerializer(shiftcode, many=True)
    return JsonResponse(serializer.data, safe=False)

  elif request.method == 'POST':
    shiftcode_data = JSONParser().parse(request)
    serializer = ShiftCodeSerializer(data=shiftcode_data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse("Add Successfully.", safe=False)
    return JsonResponse("Failed to Add.", safe=False)

  elif request.method == 'PUT':
    shiftcode_data = JSONParser().parse(request)
    shiftcode = ShiftCode.objects.get(id=shiftcode_data['id'])
    serializer = ShiftCodeSerializer(shiftcode,data=shiftcode_data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse("Update Successfully.", safe=False)
    return JsonResponse("Failed to update.", safe=False)

  elif request.method == 'DELETE':
      shiftcode_data = JSONParser().parse(request)
      shiftcode = ShiftCode.objects.get(id=shiftcode_data['id'])
      shiftcode.delete()
      return JsonResponse("Delete Successfully.", safe=False)
