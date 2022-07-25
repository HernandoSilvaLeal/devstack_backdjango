from django.urls import path, include
from django.views.generic import TemplateView
from profiles_api import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='main/index.html')),
    path('hello-view/', views.HelloApiView.as_view()),                  # el endpoint me llama a la vista, pero traigo como funcion agregando as_views
    
]
