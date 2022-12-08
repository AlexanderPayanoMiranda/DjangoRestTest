from rest_framework import serializers
from MyAPI.models import Pais
# from .models import Pais


class PaisSerializador(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ('nombre', 'moneda')
