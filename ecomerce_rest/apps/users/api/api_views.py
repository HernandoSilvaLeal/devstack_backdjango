from rest_framework.response import Response            # Importo Response para responder la data en el json del return
from rest_framework.views import APIView                # Importo APIView para hacer vistas personalizadas complejas
from apps.users.models import User                      # Importo el modelo que voya usar para la consulta de datos de la BD
from apps.users.api.serializers import UserSerializer   # Importo el serializador para transformar la data de la BD a JSON

from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])                # Agrupacion de metodos generales sin pk
def user_api_view(request):                                         # Logica REQUEST-GET, la envio, consulta db, serializa y responde json con HTTP code.
    if request.method == 'GET':
        users = User.objects.all()
        users_serializers = UserSerializer(users, many = True)
        return Response(users_serializers.data)

    elif request.method =='POST':                                   # Logica REQUEST-POST, le envio json, valida si json=serializador, guarda la data en db, responde HTTP code.
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)

@api_view(['GET','PUT','DELETE'])                                   # Agrupacion de metodos especificos con pk
def user_detail_api_view(request,pk=None):
   if request.method =='GET':                                       # Logica REQUEST-GET le envio pk, filtra para otener el id, serializa a json y responde HTTP code.
        user=User.objects.filter(id=pk).first()
        user_serializer=UserSerializer(user)
        return Response(user_serializer.data)

   elif request.method == 'PUT':                                    # Logica REQUEST-PUT le envio data + pk, filtra para otener el id, verifica que data = request.data, serializa j json, user es la instancia a actualziar, si validacion es verdadera, actualzia y responde.
        user = User.objects.filter(id=pk).first()   
        user_serializer = UserSerializer(user,data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)
                       
   elif request.method == 'DELETE':
        user=User.objects.filter(id=pk).first()
        user.delete()
        return Response('Eliminado')










# class UserAPIView(APIView):                                       # Esta forma con APIView es utilizando clases y dentro de ella una funcion por cada metodo.
#     def get(self, request):
#         users = User.objects.all()
#         users_serializer = UserSerializer(users,many=True)        # Si obtengo un listado que quiero serializar, debo usar el atributo Many
#         return Response(users_serializer.data)
