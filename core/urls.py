from django.contrib import admin
from django.urls import path, include, re_path

# Imports agregados para doc swagger
from rest_framework import permissions      
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Funcion agregada para doc swagger, info general.
schema_view = get_schema_view(
   openapi.Info(
      title="Documentacion de API DevStack Backend",
      default_version='v1',
      description="Esta es la documentacion de api para el proyecto Sena ADSI DevStack, en el backend ",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="devstackproject@gmail.com"),
      license=openapi.License(name="Proyecto Licenciado por Sena Rionegro"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [                                                  # Se anidan los urls de las apps
    path('', include('profiles_api.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('profiles_api.urls')),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'), # Visual en formato Json
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), # Visual en formato swagger standard
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), # Visual en formato redoc
]


"""core URL Configuration
s
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""