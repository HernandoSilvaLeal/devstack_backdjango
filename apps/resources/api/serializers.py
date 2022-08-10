from rest_framework import serializers
from apps.resources.api.models import *

class HelpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpsModel
        fields = '__all__'

class ResourcecategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourcecategoryModel
        fields = '__all__'

class ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourcesModel
        fields = '__all__'


# HelpsModel
# ResourcecategoryModel
# ResourcesModel

# HelpsSerializer
# ResourcecategorySerializer
# ResourcesSerializer

