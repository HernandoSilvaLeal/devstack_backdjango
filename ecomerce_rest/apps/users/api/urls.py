from django.urls import path
# from apps.users.api.api_views import UserAPIView
from apps.users.api.api_views import user_api_view, user_detail_api_view

urlpatterns = [
    # path('usuario/', UserAPIView.as_view(), name = 'usuario_api') # El path es = (Endpoint, Funcion que llama la vista, nombre del path) FORMA APIVIEW-CLASES Y FUNCIONES POR METODO
    path('usuario/', user_api_view, name = 'usuario_api'), # FORMA APIVIEW-DECORADORES Y CONDICIONALES POR METODO, importo la propia funcion, sin .as_view
    path('usuario/<int:pk>/', user_detail_api_view  , name = 'user_detail_api_view') 
]
