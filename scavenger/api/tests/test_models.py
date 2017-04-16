from django.test import TestCase

from scavenger.api.models import Building, Room, Group, Person


class BuildingModelTest(TestCase):
    """Test suite for building model."""

    def test_string_representation(self):
        building = Building(number='22', name='University Commons')
        self.assertEqual(str(building), '22')


class RoomModelTest(TestCase):
    """Test suite for room model."""

    def test_string_representation(self):
        building = Building(number='22', name='University Commons')
        room = Room(building=building, number='255',
                    name='Nautilus Chamber')
        self.assertEqual(str(room), '22/255')


class GroupModelTest(TestCase):
    """Test suite for group model."""

    def test_string_representation(self):
        group = Group(name='Department of Computer Science')
        self.assertEqual(str(group), 'Department of Computer Science')


class PersonModelTest(TestCase):
    """Test suite for person model."""

    def test_string_representation_with_prefix(self):
        person = Person(first_name='Bernd', last_name='Owsnicki-Klewe',
                        prefix='Dr')
        self.assertEqual(str(person), 'Dr. Bernd Owsnicki-Klewe')

    def test_string_representation_without_prefix(self):
        person = Person(first_name='Anthony', last_name='Pinto')
        self.assertEqual(str(person), 'Anthony Pinto')
