# Import de terceros con el manejador de rutas por defecto que ramifica los endpoits desde la URL principal
from rest_framework.routers import DefaultRouter        

# Import locales para disponibilizar las vistas                                                        

# Importa las vistas locales de la app
from apps.assets.api.views import AssetsViewSet, PhysicalassetsViewSet, InformationassetsViewSet, ServiceassetsViewSet, PersonalassetsViewSet             

# Carga la variable principal de enrutamiento
router = DefaultRouter()                                

# Zona assets del arbol de enrutamiento (endpoint disponibilizado)
router.register(r'assets', AssetsViewSet, basename = 'assets')
router.register(r'physicalassets', PhysicalassetsViewSet, basename = 'physicalassets')
router.register(r'informationassets', InformationassetsViewSet, basename = 'informationassets')
router.register(r'serviceassets', ServiceassetsViewSet, basename = 'serviceassets')
router.register(r'personalassets', PersonalassetsViewSet, basename = 'personalassets')

# Iguala las ramificaciones normales de urlpatters a la ramificacion tipo router
urlpatterns = router.urls                               