# Import de terceros con el manejador de rutas por defecto que ramifica los endpoits desde la URL principal
from rest_framework.routers import DefaultRouter        

# Import locales para disponibilizar las vistas

# Importa las vistas locales de la app
from apps.activities.api.views import ActivitiesViewSet, ControlsViewSet, RisksViewSet, ThreatsViewSet, ResultsViewSet

# Carga la variable principal de enrutamiento
router = DefaultRouter()                                

# Zona activities del arbol de enrutamiento (endpoint disponibilizado)
router.register(r'activities', ActivitiesViewSet, basename = 'activities') 
router.register(r'controls', ControlsViewSet, basename = 'controls')
router.register(r'results', ResultsViewSet, basename = 'results')
router.register(r'risks', RisksViewSet, basename = 'risks')
router.register(r'threats', ThreatsViewSet, basename = 'threats')

# Iguala las ramificaciones normales de urlpatters a la ramificacion tipo router
urlpatterns = router.urls                               