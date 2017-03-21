from django.db import models

class Building(models.Model):
    """Represents a building."""
    # 🙋 UWF uses numeric characters to identify buildings
    # 💁 'number' can be changed to reflect your campus' main identifier
    number = models.CharField(max_length=4)
    name = models.CharField(max_length=100)
    alternative_name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.number

class Room(models.Model):
    """Represents a single room in a Building."""
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    number = models.CharField(max_length=5)
    name = models.CharField(max_length=100, blank=True)
    # 🤔 Should I include a room_type (classroom, lab, office, etc.) attribute?

    def __str__(self):
        # 🤓 Rooms will be displayed as building/room number. Ex: 58A/101
        return '{}/{}'.format(self.building, self.number)
