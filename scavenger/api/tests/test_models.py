from django.test import TestCase

from scavenger.api.models import Building, Room, Group, Person


class BuildingModelTest(TestCase):
    """Test suite for building model."""

    def test_string_representation(self):
        building = Building(number='22', name='University Commons',
                            alternative_name='Commons',
                            description='Home of Student Involvement')
        self.assertEqual(str(building), '22')


class RoomModelTest(TestCase):
    """Test suite for room model."""

    def setUp(self):
        self.building = Building(number='22', name='University Commons')

    def test_string_representation(self):
        room = Room(building=self.building, number='255', floor='2',
                    name='Nautilus Chamber',
                    description='Large meeting room')
        self.assertEqual(str(room), '22/255')


class GroupModelTest(TestCase):
    """Test suite for group model."""

    def setUp(self):
        self.building = Building(number='4',
                                 name='College of Science and Engineering')
        self.room = Room(building=self.building, number='223', floor='2')

    def test_string_representation(self):
        group = Group(name='Department of Computer Science',
                      description='Faculty and Staff', location=self.room)
        self.assertEqual(str(group), 'Department of Computer Science')


class PersonModelTest(TestCase):
    """Test suite for person model."""
    # TODO: Add code to test a person's groups.

    def setUp(self):
        self.building = Building(number='4',
                                 name='College of Science and Engineering')
        self.room = Room(building=self.building, number='223', floor='2')

    def test_string_representation_with_prefix(self):
        person = Person(first_name='Bernd', last_name='Owsnicki-Klewe',
                        prefix='Dr', description='Lecturer',
                        location=self.room)
        self.assertEqual(str(person), 'Dr. Bernd Owsnicki-Klewe')

    def test_string_representation_without_prefix(self):
        person = Person(first_name='Anthony', last_name='Pinto',
                        description='Lecturer', location=self.room)
        self.assertEqual(str(person), 'Anthony Pinto')

    def test_verbose_name_plural(self):
        self.assertEqual(str(Person._meta.verbose_name_plural), 'people')
