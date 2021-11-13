from rest_framework import serializers
from app.models import TimeRecord

from app import models
from app.models.employee import Employee
from app.serializers.employee import EmployeeSerializer

class TimeRecordSerializer(serializers.ModelSerializer):
  
  emp = serializers.PrimaryKeyRelatedField(many=True, 
                     queryset=models.Employee.objects.all())

  class Meta:
    model = TimeRecord
    fields = '__all__'
    extra_kwargs = {'timerecords': {'required': False}}

  def to_representation(self, instance):
    representation = super(TimeRecordSerializer, self).to_representation(instance)
    representation['employee'] = EmployeeSerializer(instance.emp.all(), many=True).data
    return representation 
  