# Imports nativos para disponibilizar tipos de campos
from django.contrib import admin                        
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings             
from django.views.static import serve

# Imports de terceros (SWAGGER) para documentacion
from rest_framework import permissions                  
from drf_yasg.views import get_schema_view              
from drf_yasg import openapi

# Imports de terceros (JWT) para permisos y tokens
from rest_framework_simplejwt.views import (            
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# Imports local de CLASES para Login y Logout
from apps.users.views import Login,Logout               

# Configuracion en cabecera Swagger docs
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

# Arbol de enrutamiendo de endpoints

urlpatterns = [

    # Paths para la documentacion swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    # Paths para visualizar el admin de django y render de prueba
    path('', TemplateView.as_view(template_name="main/index.html")),
    path('admin/', admin.site.urls),

    # Paths de funcionamiento login y logout con jwt
    path('logout/', Logout.as_view(), name = 'logout'),
    path('login/',Login.as_view(), name = 'login'),

    # Patch para la configuracion JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # Se le envia User y pass y retorna token access y token refresh
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Refresca un token nuevo con el refresh anterior.
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


    # Paths de las 7 apps con sus enrutamientos
    path('activities/',include('apps.activities.api.routers')),
    path('assets/',include('apps.assets.api.routers')),
    path('metrics/',include('apps.metrics.api.routers')),
    path('projects/',include('apps.projects.api.routers')),
    path('resources/',include('apps.resources.api.routers')),
    path('standards/',include('apps.standards.api.routers')),
    path('users/',include('apps.users.api.routers')),
]









"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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