from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token
from rest_framework.exceptions import AuthenticationFailed

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth import logout, login

from app.models import Employee

@csrf_exempt
# @csrf_protect
# @requires_csrf_token
def login_api(request):  # /auth/login
  email = request.POST['email']
  password = request.POST['password']

  if Employee.objects.filter(Q(email=email) & Q(password=password)).exists():  # has employee in database
    user = authenticate(email, password)
    login(request, user) # login with user id
  else:
    return AuthenticationFailed('Not found user')
  
def logout_api(request):  # /auth/logout
  logout(request)

def authenticate(email, password):
  return Employee.objects.get(email=email, password=password)