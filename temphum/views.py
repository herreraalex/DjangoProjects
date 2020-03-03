from rest_framework import viewsets
from .models import Temphum
from .serializers import TemphumSerializer

class TemphumViewSet(viewsets.ModelViewSet):
    queryset = Temphum.objects.all().order_by('-created')
    serializer_class = TemphumSerializer
