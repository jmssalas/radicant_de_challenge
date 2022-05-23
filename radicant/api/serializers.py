from rest_framework import serializers
from .models import Etf, Filter

class EtfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etf
        fields = ['fund_symbol', 'fund_category', 'size_type']

class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter
        fields = ['fund_category', 'size_type']