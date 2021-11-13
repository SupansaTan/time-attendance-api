from rest_framework import serializers
from app.models import PlanShift

from app import models
from app.models.employee import Employee
from app.serializers.employee import EmployeeSerializer


from app.serializers.employee import EmployeeSerializer

class PlanShiftSerializer(serializers.ModelSerializer):
  
  emp = serializers.PrimaryKeyRelatedField(many=True, 
                     queryset=models.Employee.objects.all())

  class Meta:
    model = PlanShift
    fields = '__all__'
    extra_kwargs = {'planshifts': {'required': False}}

  def to_representation(self, instance):
    representation = super(PlanShiftSerializer, self).to_representation(instance)
    representation['employee'] = EmployeeSerializer(instance.emp.all(), many=True).data
    return representation 
