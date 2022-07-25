from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30) # Serializacion del campo para probar nuestro api view
    