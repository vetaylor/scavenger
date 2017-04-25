from rest_framework import serializers

from .models import Building, Room, Group, Person


class BuildingSerializer(serializers.ModelSerializer):
    """Serializer for Building model."""
    class Meta:
        model = Building
        fields = ('number', 'name', 'alternative_name', 'description',)


class RoomSerializer(serializers.ModelSerializer):
    """Serializer for Room model."""
    class Meta:
        model = Room
        fields = ('building', 'number', 'name', 'description',)


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for Group model."""
    class Meta:
        model = Group
        fields = ('name', 'description', 'location',)


class PersonSerializer(serializers.ModelSerializer):
    """Serializer for Person model."""
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'prefix', 'description', 'groups',
                  'location',)
