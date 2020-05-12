from rest_framework import viewsets
from .models import Temphum, Cultivo
from .serializers import TemphumSerializer, CultivoSerializer

class TemphumViewSet(viewsets.ModelViewSet):
    queryset = Temphum.objects.all().order_by('-created')
    serializer_class = TemphumSerializer

class CultivoViewSet(viewsets.ModelViewSet):
    queryset = Cultivo.objects.all().order_by('-created')
    serializer_class = CultivoSerializer
