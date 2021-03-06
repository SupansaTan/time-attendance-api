from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny

from app.models import PlanShift, ShiftCode
from app.serializers import PlanShiftSerializer

from django.db.models import Q

import datetime

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
# GET plan data from employee id

def plan_list(request, param_id=0):
    if request.method == 'GET':
        planshift = PlanShift.objects.all()
        serializer = PlanShiftSerializer(planshift, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        plan = JSONParser().parse(request)
        employee_all = plan["employee_list"]
        start_date = datetime.datetime.strptime(plan["start_date"], "%Y-%m-%d")
        end_date = datetime.datetime.strptime(plan["end_date"], "%Y-%m-%d")
        date = start_date

        ot_exist = 'overtime' in plan.keys()
        shifttime_exist = 'start_time' in plan.keys()

        while end_date >= date:
            for employee_id in employee_all:
                # assign both
                if(ot_exist & shifttime_exist):
                    shiftcode = ShiftCode.objects.get(start_time=plan['start_time'])
                    start_time = shiftcode.start_time
                    end_time = shiftcode.end_time
                    planshift_data = {
                                        "date": datetime.datetime.strftime(date, "%Y-%m-%d"),
                                        "employee": [employee_id],
                                        "department": plan["department"],
                                        "overtime": plan["overtime"],
                                        "start_time": start_time.strftime("%H:%M:%S"),
                                        "end_time": end_time.strftime("%H:%M:%S"),
                                    }
                # assign ot
                elif(ot_exist):
                    planshift_data = {
                                        "date": datetime.datetime.strftime(date, "%Y-%m-%d"),
                                        "employee": [employee_id],
                                        "department": plan["department"],
                                        "overtime": plan["overtime"],
                                    }
                # assign shift time
                elif(shifttime_exist):
                    shiftcode = ShiftCode.objects.get(start_time=plan['start_time'])
                    start_time = shiftcode.start_time
                    end_time = shiftcode.end_time
                    planshift_data = {
                                        "date": datetime.datetime.strftime(date, "%Y-%m-%d"),
                                        "employee": [employee_id],
                                        "department": plan["department"],
                                        "start_time": start_time.strftime("%H:%M:%S"),
                                        "end_time": end_time.strftime("%H:%M:%S"),
                                    }
                try :
                    data_exist = PlanShift.objects.get(date=planshift_data["date"],employee=employee_id)
                    serializer = PlanShiftSerializer(data_exist ,data=planshift_data)
                except :
                    serializer = PlanShiftSerializer(data=planshift_data)
                if serializer.is_valid():
                    serializer.save()     
            date += datetime.timedelta(days=1)
        return JsonResponse("Add Successfully.", safe=False)

    elif request.method == 'DELETE':
        plan_data = PlanShift.objects.get(id=param_id)
        plan_data.delete()
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