from rest_framework import serializers
from apps.assets.api.models import *

class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetsModel
        fields = '__all__'

class PhysicalassetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalassetsModel
        fields = '__all__'

class InformationassetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationassetsModel
        fields = '__all__'

class ServiceassetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceassetsModel
        fields = '__all__'

class PersonalassetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalassetsModel
        fields = '__all__'


# AssetsModel
# PhysicalassetsModel
# InformationassetsModel
# ServiceassetsModel
# PersonalassetsModel

# AssetsSerializer
# PhysicalassetsSerializer
# InformationassetsSerializer
# ServiceassetsSerializer
# PersonalassetsSerializer