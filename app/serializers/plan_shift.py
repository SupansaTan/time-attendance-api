from rest_framework import serializers
from app.models import PlanShift

from app.serializers.employee import EmployeeSerializer

class PlanShiftSerializer(serializers.ModelSerializer):
  class Meta:
    model = PlanShift
    fields = '__all__'

  def to_representation(self, instance):
    self.fields['emp'] =  EmployeeSerializer(read_only=True)
    return super(PlanShiftSerializer, self).to_representation(instance)