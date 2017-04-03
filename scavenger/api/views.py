from django.shortcuts import render

from rest_framework import viewsets

from .models import Building, Room, Group, Person
from .serializers import BuildingSerializer, RoomSerializer, GroupSerializer, PersonSerializer

class BuildingViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing Building objects."""
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class RoomViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing Room objects."""
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing Group objects."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PersonViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing Person objects."""
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
