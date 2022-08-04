from rest_framework import serializers
from apps.metrics.api.models import *

class ProgressreportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressreportModel
        fields = '__all__'

class IndicatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndicatorsModel
        fields = '__all__'

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarModel
        fields = '__all__'


# ProgressreportModel
# IndicatorsModel
# CalendarModel

# ProgressreportSerializer
# IndicatorsSerializer
# CalendarSerializer
