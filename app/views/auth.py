from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth import logout, login

from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

from app.models import Employee

@api_view(["POST"])
@permission_classes([AllowAny])
def login_api(request):  # /auth/login
  email = request.POST['email']
  password = request.POST['password']

  if Employee.objects.filter(Q(email=email) & Q(password=password)).exists():  # has employee in database
    user = authenticate(email, password)
    token = Token.objects.get_or_create(user=user)[0].key

    data = {}
    data["token"] = token
    res = {
      'data': data,
      'message': 'login succeesful',
      'status': 200
    }
    return JsonResponse(res, safe=False)
  else:
    return JsonResponse({'message': "Failed to get current user."}, safe=False, status=500)
  
@api_view(["GET"])
def logout_api(request):  # /auth/logout
  request.user.auth_token.delete()
  logout(request)

def getCurrentUserRole(request):  # /auth/getCurrentUserRole
  token = request.META.get('HTTP_AUTHORIZATION')

  if Token.objects.filter(key=token).exists():
    user = Token.objects.get(key=token).user_id
    emp = Employee.objects.get(user_id=user)
    
    data = {}
    data['employee_id'] = emp.id
    data['role'] = emp.role
    res = {
      'data': data,
      'message': 'succeesful',
      'status': 200
    }
    return JsonResponse(res, safe=False)

  else:
    return JsonResponse({'message':"Failed to get current user."}, safe=False, status=500)

def authenticate(email, password):
  return Employee.objects.get(email=email, password=password).user