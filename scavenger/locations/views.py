from django.shortcuts import render
from rest_framework import viewsets
from .models import Building, Room
from .serializers import BuildingSerializer, RoomSerializer

class BuildingViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing Building objects."""
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class RoomViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing Room objects."""
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
