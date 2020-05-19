from django.db import models
import uuid

class Temphum(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(verbose_name='Tipo', max_length=20)
    value = models.IntegerField(verbose_name='Valor')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

CULTIVO_CHOICES = (
    ('Leche','Leche'),
    ('Cacao','Cacao'),
    ('Carnes','Carnes'),
    ('Flores', 'Flores'),
    ('Hortalizas', 'Hortalizas')
)

class Cultivo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(verbose_name='codigo', max_length=40)
    latitud = models.IntegerField(verbose_name='latitud')
    longitud = models.IntegerField(verbose_name='longitud')
    producto = models.CharField(verbose_name = 'producto', max_length = 30,choices = CULTIVO_CHOICES, default='Leche')
    validacion = models.PositiveIntegerField(verbose_name='validacion')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)