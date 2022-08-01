from rest_framework.response import Response            # Importo Response para responder la data en el json del return
from rest_framework.views import APIView                # Importo APIView para hacer vistas personalizadas complejas
from apps.users.models import User                      # Importo el modelo que voya usar para la consulta de datos de la BD
from apps.users.api.serializers import UserSerializer   # Importo el serializador para transformar la data de la BD a JSON

class UserAPIView(APIView):

    def get(self, request):
        users = User.objects.all()
        users_serializer = UserSerializer(users,many=True)      # Si obtengo un listado que quiero serializar, debo usar el atributo Many
        return Response(users_serializer.data)
