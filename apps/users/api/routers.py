from rest_framework.routers import DefaultRouter        # Import de terceros con el manejador de rutas por defecto que ramifica los endpoits desde la URL principal

                                                        # Import locales para disponibilizar las vistas

from apps.users.api.views import UserViewSet            # Importa las vistas locales de la app

router = DefaultRouter()                                # Carga la variable principal de enrutamiento

                                                        # Zona USERS del arbol de enrutamiento (endpoint disponibilizado)
router.register('', UserViewSet, basename="users")      

urlpatterns = router.urls                               # Iguala las ramificaciones normales de urlpatters a la ramificacion tipo router