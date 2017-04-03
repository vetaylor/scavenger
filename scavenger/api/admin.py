from django.contrib import admin

from .models import Building, Room, Group, Person

admin.site.register(Building)
admin.site.register(Room)
admin.site.register(Group)
admin.site.register(Person)
