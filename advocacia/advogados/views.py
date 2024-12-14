# advogados/views.py
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Advogado
from .serializers import AdvogadoSerializer

# API ViewSet
class AdvogadoViewSet(ModelViewSet):
    queryset = Advogado.objects.all()
    serializer_class = AdvogadoSerializer

# View para renderizar HTML
def lista_advogados(request):
    advogados = Advogado.objects.all()
    return render(request, 'advogados/advogados.html', {'advogados': advogados})
