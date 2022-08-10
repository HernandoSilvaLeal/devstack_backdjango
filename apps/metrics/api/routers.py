# Import de terceros con el manejador de rutas por defecto que ramifica los endpoits desde la URL principal
from rest_framework.routers import DefaultRouter        

# Import locales para disponibilizar las vistas

# Importa las vistas locales de la app
from apps.metrics.api.views import ProgressreportViewSet, IndicatorsViewSet, CalendarViewSet

# Carga la variable principal de enrutamiento
router = DefaultRouter()                                

# Zona metrics del arbol de enrutamiento (endpoint disponibilizado)
router.register(r'progressreport', ProgressreportViewSet, basename = 'progressreport')
router.register(r'indicators', IndicatorsViewSet, basename = 'indicators')
router.register(r'calendar', CalendarViewSet, basename = 'calendar')

# Iguala las ramificaciones normales de urlpatters a la ramificacion tipo router
urlpatterns = router.urls                               