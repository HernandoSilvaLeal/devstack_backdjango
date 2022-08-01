from rest_framework import serializers      # Importo los serializers del framework
from apps.users.models import User          # Importo el modelo que voy a serializar


class UserSerializer(serializers.ModelSerializer): # Por convencion se le coloca el nombre del modelo al que hace referencia y luego Serializer y hereda de model serializar porque es un MODELO
    class Meta:
        model = User
        # fields = '__all__'                         # Se utiliza fields o exclude, para señalar los campos, para campos especificos usar []
        fields = ['id','password','username','email','name','last_name']
    
    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
