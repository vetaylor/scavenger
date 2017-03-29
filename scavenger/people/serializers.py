from rest_framework import serializers
from .models import Group, Person

class GroupSerializer(serializers.ModelSerializer):
    """Serializer for Group model."""
    class Meta:
        model =  Group
        fields = ("name",)

class PersonSerializer(serializers.ModelSerializer):
    """Serializer for Person model."""
    class Meta:
        model = Person
        fields = ("first_name", "last_name", "prefix", "groups")
