from rest_framework import serializers
from .models import Building, Room

class BuildingSerializer(serializers.ModelSerializer):
    """Serializer for Building model."""
    class Meta:
        model = Building
        fields = ("number", "name", "alternative_name", "description")

class RoomSerializer(serializers.ModelSerializer):
    """Serializer for Room model."""
    class Meta:
        model = Room
        fields = ("building", "number", "name")
