from rest_framework.routers import DefaultRouter        # Import de terceros con el manejador de rutas por defecto que ramifica los endpoits desde la URL principal

                                                        # Import locales para disponibilizar las vistas

from apps.users.api.views import UserViewSet            # Importa las vistas locales de la app

router = DefaultRouter()                                # Carga la variable principal de enrutamiento

                                                        # Zona XXXXXXX del arbol de enrutamiento (endpoint disponibilizado)
router.register(r'assets', AssetsViewSet, basename = 'assets')
router.register(r'physicalassets', PhysicalassetsViewSet, basename = 'physicalassets')
router.register(r'informationassets', InformationassetsViewSet, basename = 'informationassets')
router.register(r'serviceassets', ServiceassetsViewSet, basename = 'serviceassets')
router.register(r'personalassets', PersonalassetsViewSet, basename = 'personalassets')

urlpatterns = router.urls                               # Iguala las ramificaciones normales de urlpatters a la ramificacion tipo router