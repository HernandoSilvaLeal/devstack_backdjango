from django.urls import path, include
from django.views.generic import TemplateView
from profiles_api import views

from rest_framework.routers import DefaultRouter                                    # Esta importacion permite gestionar metodos tipo GENERICOS viewset.


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename = 'hello-viewset')    # (1) enpoint, (2) clase de views que apunta, (3) Sobrenombre 


urlpatterns = [
    path('templateExample/', TemplateView.as_view(template_name='main/index.html')),
    path('hello-view/', views.HelloApiView.as_view()),                               # el endpoint me llama a la vista, pero traigo como funcion agregando as_views
    path('', include(router.urls)),                                                  # registro de todos los router dentro del urlpatters, el '' se sobrescribe y breves.

]