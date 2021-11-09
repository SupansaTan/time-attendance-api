from rest_framework import serializers
from app.models import ShiftCode

class ShiftCodeSerializer(serializers.ModelSerializer):
  class Meta:
    model = ShiftCode
    fields = '__all__'