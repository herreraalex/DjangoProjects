import requests
from rest_framework import viewsets
from .models import Temphum
from .serializers import TemphumSerializer
from django.shortcuts import render, HttpResponse


#class TemphumViewSet(viewsets.ModelViewSet):
#    queryset = Temphum.objects.all().order_by('-created')
#    serializer_class = TemphumSerializer

def home(request):
        return render(request, "temphum/temphum.html")

def temphum(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'value' in request.GET:
        value = request.GET['value']
        # Verifica si el value no esta vacio
        if value:
            # Crea el json para realizar la petición POST al Web Service
            args = {'type': 'ph', 'value': value}
            response = requests.post('http://127.0.0.1:8000/measures/', args)
            # Convierte la respuesta en JSON
            measure_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/measures/')
    # Convierte la respuesta en JSON
    measures = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "temphum/temphum.html", {'measures': measures})