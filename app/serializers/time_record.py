from rest_framework import serializers
from app.models import TimeRecord

from app.serializers.employee import EmployeeSerializer

class TimeRecordSerializer(serializers.ModelSerializer):
  class Meta:
    model = TimeRecord
    fields = '__all__'

  def to_representation(self, instance):
    self.fields['emp'] =  EmployeeSerializer(read_only=True)
    return super(TimeRecordSerializer, self).to_representation(instance)
  