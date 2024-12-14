from django.contrib import admin
from django.urls import path, include

# Importações das views de cada app
from advogados import views as advogados_views
from documentos import views as documentos_views  # Certifique-se de importar as views de documentos

# Importando a view para a página inicial (home)
from . import views  # Aqui você importa a view home

from rest_framework.routers import DefaultRouter
from documentos.views import DocumentoViewSet  # Importa o viewset para documentos
from advogados.views import AdvogadoViewSet  # Importa o viewset para advogados

# Criação do router
router = DefaultRouter()
router.register(r'documentos', DocumentoViewSet, basename='documento')
router.register(r'advogados', AdvogadoViewSet, basename='advogado-api-list')

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para o admin
    path('documentos/', documentos_views.documentos, name='lista_documentos'),  # Página de documentos
    path('advogados/', advogados_views.lista_advogados, name='advogado-list'),  # Página HTML dos advogados
    path('api/', include(router.urls)),  # Incluindo as rotas das APIs para documentos e advogados
    path('', views.home, name='home'),  # Página inicial
]

# Configurações para servir arquivos estáticos em modo DEBUG
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
