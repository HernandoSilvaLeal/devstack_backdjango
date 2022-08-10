# Import de terceros con el manejador de rutas por defecto que ramifica los endpoits desde la URL principal
from rest_framework.routers import DefaultRouter        

# Import locales para disponibilizar las vistas                                                        

# Importa las vistas locales de la app
from apps.resources.api.views import HelpsViewSet, ResourcecategoryViewSet, ResourcesViewSet       

# Carga la variable principal de enrutamiento
router = DefaultRouter()                                

# Zona resources del arbol de enrutamiento (endpoint disponibilizado)
router.register(r'helps', HelpsViewSet, basename = 'helps')
router.register(r'resourcecategory', ResourcecategoryViewSet, basename = 'resourcecategory')
router.register(r'resources', ResourcesViewSet, basename = 'resources')

# Iguala las ramificaciones normales de urlpatters a la ramificacion tipo router
urlpatterns = router.urls                               