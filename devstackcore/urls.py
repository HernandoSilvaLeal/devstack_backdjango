from django.contrib import admin                        # Import nativo del admin de django que disponibiliza tipos de campos
from django.urls import path, include, re_path          # Import nativo los path de las url, el repath es para ejecir entre rutas y el include para ramificar el programa.
from django.conf import settings                        # Import nativo de settings para poder leer y cargar las configuraciones de django con las variables de base.py
from django.views.static import serve

from drf_yasg.views import get_schema_view              # Import de terceros necesaria para que funcione documentacion de swagger
from drf_yasg import openapi                            # Import de terceros necesaria para que funcione documentacion de swagger

from rest_framework import permissions                  # Import de terceros necesario para que funcione permisos y tokens jwt
from rest_framework_simplejwt.views import (            # Import de terceros necesario para que funcione permisos y tokens jwt, el normal y el refresh
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.users.views import Login,Logout               # Import local de CLASES para disponibilizar el Login y Logout

schema_view = get_schema_view(                          # Parametros de configuracion en cabecera swagger documentacion
   openapi.Info(
      title="Documentación de API",
      default_version='v0.1',
      description="Documentación pública de API de Ecommerce",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="developerpeperu@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# Arbol de enrutamiendo de endpoints

urlpatterns = [

    # Paths para la documentacion swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Paths para visualizar el admin de django.
    path('admin/', admin.site.urls),

    # Paths de funcionamiento login y logout con jwt
    path('logout/', Logout.as_view(), name = 'logout'),
    path('login/',Login.as_view(), name = 'login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

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