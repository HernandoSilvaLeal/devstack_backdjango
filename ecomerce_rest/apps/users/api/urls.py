from django.urls import path
from apps.users.api.api_views import UserAPIView

urlpatterns = [
    path('usuario/', UserAPIView.as_view(), name = 'usuario_api') # El path es = (Endpoint, Funcion que llama la vista, nombre del path)
]
