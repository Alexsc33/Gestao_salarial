from rest_framework import serializers
from .models import Contato

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'