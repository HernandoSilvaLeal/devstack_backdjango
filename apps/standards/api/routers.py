# Import de terceros con el manejador de rutas por defecto que ramifica los endpoits desde la URL principal
from rest_framework.routers import DefaultRouter        

# Import locales para disponibilizar las vistas

# Importa las vistas locales de la app
from apps.standards.api.views import UserViewSet            

# Carga la variable principal de enrutamiento
router = DefaultRouter()

# Zona standards del arbol de enrutamiento (endpoint disponibilizado)
router.register(r'standards', StandardsViewSet, basename = 'helps')
router.register(r'chapters', ChaptersViewSet, basename = 'chapters')
router.register(r'articles', ArticlesViewSet, basename = 'articles')

# Iguala las ramificaciones normales de urlpatters a la ramificacion tipo router
urlpatterns = router.urls                               