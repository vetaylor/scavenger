from rest_framework import serializers
from .models import Person, Group

class PersonSerializer(serializers.ModelSerializer):
    """Serializer for Person model."""
    class Meta:
        model = Person

class GroupSerializer(serializers.ModelSerializer):
    """Serializer for Group model."""
    class Meta:
        model =  Group
