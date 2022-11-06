from .models import ParkingLot
from .models import Corner
from rest_framework import serializers

class ParkingLotSerializer(serializers.ModelSerializer):
    class Meta:
        model=ParkingLot
        fields='__all__'

class CornerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Corner
        fields='__all__'
    