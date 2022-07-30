from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    namep = serializers.CharField(max_length=50) # Serializacion del campo para probar nuestro api view
    # name2 = serializers.CharField(max_length=50) # Por defecto los campos son obligatorios
    