from rest_framework.views import APIView       # 
from rest_framework.response import Response   # 

# 

class HelloApiView(APIView):                           # Clase de Api View de Prueba

    def get(self, request, format=None):         # Funcion para retornar lista de caracteristicas de ApiView
        an_apiview = [
            'Usame metodos HTTP como funciones (get, post, put, delete)',
            'es similar a una vista tradicional de Django',
            'Nos da mayor control sobre la logica de nuestra app',
            'Esta mapeado manualmente a los URLs',
        ]

        return Response({                       # Esta info se convierte a JSON, debe ser lista o Dict
            'message':'Hello',
            'an_apiview': an_apiview,
            }) 
        















