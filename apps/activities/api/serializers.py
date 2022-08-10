from rest_framework import serializers
from apps.activities.api.models import *

class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivitiesModel
        fields = '__all__'

class ControlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlsModel
        fields = '__all__'

class RisksSerializer(serializers.ModelSerializer):
    class Meta:
        model = RisksModel
        fields = '__all__'

class ThreatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreatsModel
        fields = '__all__'

class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultsModel
        fields = '__all__'


# ActivitiesSerializer
# ControlsSerializer
# RisksSerializer
# ThreatsSerializer
# ResultsSerializer

# ActivitiesModel
# ControlsModel
# RisksModel
# ThreatsModel
# ResultsModel