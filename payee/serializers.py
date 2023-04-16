from rest_framework import serializers
from .models import Payee

class PayeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payee
        fields = '__all__'

