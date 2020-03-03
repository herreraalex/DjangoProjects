from rest_framework import serializers
from .models import Temphum

class TemphumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temphum
        fields = ('id', 'type', 'value')