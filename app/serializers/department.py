from rest_framework import serializers
from app.models import Department

class DepartmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Department
    fields = ('id', 'name', 'active_employee', 'total_employee')