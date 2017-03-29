from django.test import TestCase
from .models import Building, Room

class LocationTest(TestCase):

    def setUp(self):
        # Create five buildings:
        self._004 = Building.objects.create(number="004",
            name="Hal Marcus College of Science and Engineering")
        self._22 = Building.objects.create(number="22", name="University Commons")
        self._58A = Building.objects.create(number="58A",
            name="Science Lecture Lab")
        self._82 = Building.objects.create(number="82",
            name="Center for Fine and Performing Arts")
        self._72 = Building.objects.create(number="72",
            name="Health, Leisure, & Sports Facility")

        # Create rooms:
        self._004_435 = Room.objects.create(building=self._004, number="435",
            name="Dr. OK's Office")
        self._58A_101 = Room.objects.create(building=self._58A, number="101")
