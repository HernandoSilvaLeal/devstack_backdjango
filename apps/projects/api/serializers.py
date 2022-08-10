from rest_framework import serializers
from apps.projects.api.models import *

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsModel
        fields = '__all__'

class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompaniesModel
        fields = '__all__'

class StagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StagesModel
        fields = '__all__'

class AreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreasModel
        fields = '__all__'


# ProjectsModel
# CompaniesModel
# StagesModel
# AreasModel

# ProjectsSerializer
# CompaniesSerializer
# StagesSerializer
# AreasSerializer
