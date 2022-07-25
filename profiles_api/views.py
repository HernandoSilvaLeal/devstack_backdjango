# Importaciones del framework
from rest_framework.views import APIView              # Importacion para metodos CUSTOMIZADOS
from rest_framework.response import Response          # 
from rest_framework import status                     # 
from rest_framework import viewsets                   # Importacion para metodos GENERICOS

# Importaciones del proyecto
from profiles_api import serializers                   # Importamos los serializers ya creados

class HelloApiView(APIView):                           # Clase de Api View de Prueba

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):               # Metodo para leer o retornar lista de caracteristicas de ApiView
        an_apiview = [
            'Usame metodos HTTP como funciones (get, post, put, delete)',
            'es similar a una vista tradicional de Django',
            'Nos da mayor control sobre la logica de nuestra app',
            'Esta mapeado manualmente a los URLs',
        ]

        return Response({                              # Esta info se convierte a JSON, debe ser lista o Dict
            'message':'Hello',
            'an_apiview': an_apiview,
            }) 

    def post(self, request):                           # Metodo que crea un mensaje con nuestro nombre
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
                name = serializer.validated_data.get('name')
                message = f'Hello {name}'
                return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            ) 


    def put(self, request, pk=None):                    # Actualizacion Total del Obj
        return Response ({'method':'PUT'})


    def patch(self, request, pk=None):                  # Actualizacion Parcial del Obj
        return Response ({'method':'PATCH'})


    def delete(self, request, pk=None): 
        return Response ({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):                   # El parametro el realmente un apuntador, es decir --> (archivo.ClaseTal)

    serializer_class = serializers.HelloSerializer

    def list (self, request):                           # Metodo para leer hola mundo
        
        a_viewset = [
            'Usa acciones (list, create, retrieve, update, partial_ipdate)',
            'Automaticamente mapea los URLs usando Routers',
            'Provee mas funcionalidad con menos codigo',
        ]

        return Response({                              # Esta info se convierte a JSON, debe ser lista o Dict
            'message':'Hello',
            'a_viewset': a_viewset
            }) 

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
                name = serializer.validated_data.get('name')
                message = f'Hello {name}'
                return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            ) 
    
    def retrieve(self, request, pk=None):               
        return Response ({'http_method':'GET'})           # ok lo dejamos en none porque aun no estamos trabajando con id
    
    def update(self, request, pk=None):               
        return Response ({'http_method':'PUT'})    
    
    def partial_update(self, request, pk=None):               
        return Response ({'http_method':'PATCH'})    
    
    def destroy(self, request, pk=None):               
        return Response ({'http_method':'DELETE'})    








