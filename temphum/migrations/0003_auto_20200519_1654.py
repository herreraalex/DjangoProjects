# Generated by Django 3.0.3 on 2020-05-19 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temphum', '0002_cultivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cultivo',
            name='producto',
            field=models.CharField(choices=[('Leche', 'Leche'), ('Cacao', 'Cacao'), ('Carnes', 'Carnes'), ('Flores', 'Flores'), ('Hortalizas', 'Hortalizas')], default='Leche', max_length=30, verbose_name='producto'),
        ),
    ]
