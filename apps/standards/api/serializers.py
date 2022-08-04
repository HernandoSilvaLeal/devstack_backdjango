from rest_framework import serializers
from apps.standards.api.models import *

class StandardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StandardsModel
        fields = '__all__'

class ChaptersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChaptersModel
        fields = '__all__'

class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticlesModel
        fields = '__all__'

# StandardsModel
# ChaptersModel
# ArticlesModel

# StandardsSerializer
# ChaptersSerializer
# ArticlesSerializer
