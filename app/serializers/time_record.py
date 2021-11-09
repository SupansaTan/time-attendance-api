from rest_framework import serializers
from app.models import TimeRecord

class TimeRecordSerializer(serializers.ModelSerializer):
  class Meta:
    model = TimeRecord
    fields = '__all__'