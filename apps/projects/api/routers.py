# Import de terceros con el manejador de rutas por defecto que ramifica los endpoits desde la URL principal
from rest_framework.routers import DefaultRouter        

# Import locales para disponibilizar las vistas                                                        

# Importa las vistas locales de la app
from apps.projects.api.views import ProjectsViewSet, CompaniesViewSet, StagesViewSet, AreasViewSet             

# Carga la variable principal de enrutamiento
router = DefaultRouter()                                

# Zona projects del arbol de enrutamiento (endpoint disponibilizado)
router.register(r'projects', ProjectsViewSet, basename = 'projects')
router.register(r'companies', CompaniesViewSet, basename = 'companies')
router.register(r'stages', StagesViewSet, basename = 'stages')
router.register(r'areas', AreasViewSet, basename = 'areas')

# Iguala las ramificaciones normales de urlpatters a la ramificacion tipo router
urlpatterns = router.urls                               