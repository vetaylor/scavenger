from django.db import models

class Person(models.Model):
    """Represents a person."""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    prefix = models.CharField(max_length=3, blank=True)

    def __str__(self):
        if self.prefix:
            return '{}. {} {}'.format(self.prefix, self.first_name,
                self.last_name)
        else:
            return '{} {}'.format(self.first_name, self.last_name)
