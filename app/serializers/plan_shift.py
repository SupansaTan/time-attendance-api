from rest_framework import serializers
from app.models import PlanShift

from app import models
from app.models.employee import Employee
from app.serializers.employee import EmployeeSerializer

from app.models.department import Department
from app.serializers.department import DepartmentSerializer


class PlanShiftSerializer(serializers.ModelSerializer):
  
  employee = serializers.PrimaryKeyRelatedField(many=True, 
                     queryset=models.Employee.objects.all())
        
  department = serializers.PrimaryKeyRelatedField(many=True, 
                     queryset=models.Department.objects.all())

  class Meta:
    model = PlanShift
    fields = '__all__'
    extra_kwargs = {'dep_plan': {'required': False}, 'emp_plan': {'required': False}}

  def to_representation(self, instance):
    representation = super(PlanShiftSerializer, self).to_representation(instance)
    representation['employee'] = EmployeeSerializer(instance.employee.all(), many=True).data
    representation['department'] = DepartmentSerializer(instance.department.all(), many=True).data
    return representation 
