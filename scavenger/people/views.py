from django.shortcuts import render
from rest_framework import viewsets
from .models import Person, Group
from .serializers import PersonSerializer, GroupSerializer

class PersonViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing Person objects."""
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing Group objects."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
