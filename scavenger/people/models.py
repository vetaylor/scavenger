from django.db import models

class Group(models.Model):
    """Represents a group."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Person(models.Model):
    """Represents a person."""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    prefix = models.CharField(max_length=3, blank=True)
    groups = models.ManyToManyField(Group)

    def __str__(self):
        if self.prefix is not None:
            return '{}. {} {}'.format(self.prefix, self.first_name,
                self.last_name)
        else:
            return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name_plural = "people"
