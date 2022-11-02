from django.shortcuts import render
from .models import ParkingLot
from rest_framework import viewsets
from .serializers import ParkingLotSerializer

class ParkingLotViewset(viewsets.ModelViewSet):
    serializer_class=ParkingLotSerializer
    queryset=ParkingLot.objects.all()
