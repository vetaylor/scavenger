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
        return '{}'.format(self.number)


class Room(models.Model):
    """Represents a single room in a Building."""
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    number = models.CharField(max_length=5)
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    # 🤔 Should I include a room_type (classroom, lab, office, etc.) attribute?

    def __str__(self):
        # 🤓 Rooms will be displayed as building/room number. Ex: 58A/101
        return '{}/{}'.format(self.building, self.number)


class Group(models.Model):
    """Represents a group."""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    location = models.ForeignKey(Room, blank=True, null=True,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)


class Person(models.Model):
    """Represents a person."""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    prefix = models.CharField(max_length=3, blank=True)
    description = models.TextField(blank=True)
    groups = models.ManyToManyField(Group, blank=True)
    # 🤔 What if a given person doesn't belong to a room, but to a building?
    location = models.ForeignKey(Room, blank=True, null=True,
                                 on_delete=models.CASCADE)

    def __str__(self):
        if self.prefix is '':
            return '{} {}'.format(self.first_name, self.last_name)
        else:
            return '{}. {} {}'.format(self.prefix, self.first_name,
                                      self.last_name)

    class Meta:
        verbose_name_plural = "people"
