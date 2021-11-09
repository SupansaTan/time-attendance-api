from rest_framework import serializers
from app.models import PlanShift

class PlanShiftSerializer(serializers.ModelSerializer):
  class Meta:
    model = PlanShift
    fields = '__all__'