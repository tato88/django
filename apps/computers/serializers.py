from rest_framework.serializers import ModelSerializer
from .models import ComputerModel


class ComputerSerializer(ModelSerializer):
    class Meta:
        model = ComputerModel
        fields = ('id', 'brand', 'model', 'ram', 'diagonal')
        # fields = '__all__'
