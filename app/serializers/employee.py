from rest_framework import serializers
from app import models
from app.models.employee import Employee
from app.models.department import Department
from app.serializers.department import DepartmentSerializer

class EmployeeSerializer(serializers.ModelSerializer):
      
  department = serializers.PrimaryKeyRelatedField(many=True, 
                     queryset=models.Department.objects.all())

  class Meta:
    model = Employee
    fields = '__all__'
    extra_kwargs = {'employees': {'required': False}}

  def to_representation(self, instance):
    representation = super(EmployeeSerializer, self).to_representation(instance)
    representation['department'] = DepartmentSerializer(instance.department.all(), many=True).data
    return representation 

  