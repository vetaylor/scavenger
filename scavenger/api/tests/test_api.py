from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, \
                                force_authenticate

from scavenger.api.models import Building, Room, Group, Person
from scavenger.api.views import BuildingViewSet, RoomViewSet, GroupViewSet, \
                                PersonViewSet


class BuildingAPITests(APITestCase):
    """Test suite for building api."""

    def setUp(self):
        self.user = User.objects.create_superuser('temp', 'temp@test.com',
                                                  'temp')
        self.client.login(username='temp', password='temp')
        self.factory = APIRequestFactory()

    def test_create_building(self):
        """Test the api can create a Building."""
        view = BuildingViewSet.as_view({'post': 'create'})
        data = {'number': '22', 'name': 'University Commons'}
        url = reverse('building-list')
        request = self.factory.post(url, data, format='json')
        force_authenticate(request, user=self.user)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Building.objects.count(), 1)
        self.assertEqual(Building.objects.get().number, '22')

    def test_building_list(self):
        """Test the api can list all the Buildings."""
        view = BuildingViewSet.as_view({'get': 'list'})
        url = reverse('building-list')
        request = self.factory.get(url)
        force_authenticate(request, user=self.user)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_building_detail(self):
        """Test the api can retrieve a given Building."""
        building = Building.objects.create(number='22',
                                           name='University Commons')

        view = BuildingViewSet.as_view({'get': 'retrieve'})
        url = reverse('building-detail', kwargs={'pk': building.id})
        request = self.factory.get(url)
        force_authenticate(request, user=self.user)
        response = view(request, pk=building.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_building(self):
        """Test the api can update a Building."""
        building = Building.objects.create(number='4',
                                           name='University Commons')

        view = BuildingViewSet.as_view({'put': 'update'})
        data = {'number': '4',
                'name': 'Hal Marcus College of Science and Engineering'}
        url = reverse('building-detail', kwargs={'pk': building.id})
        request = self.factory.put(url, data, format='json')
        force_authenticate(request, user=self.user)
        response = view(request, pk=building.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_building(self):
        """Test the api can delete a Building."""
        building = Building.objects.create(number='22',
                                           name='University Commons')

        view = BuildingViewSet.as_view({'delete': 'destroy'})
        url = reverse('building-detail', kwargs={'pk': building.id})
        request = self.factory.delete(url, format='json', follow=True)
        force_authenticate(request, user=self.user)
        response = view(request, pk=building.id)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class RoomAPITest(APITestCase):
    """Test suite for room api."""

    def setUp(self):
        self.user = User.objects.create_superuser('temp', 'temp@test.com',
                                                  'temp')
        self.client.login(username='temp', password='temp')
        Building.objects.create(number='22', name='University Commons')
        self.factory = APIRequestFactory()

    def test_create_room(self):
        """Test the api can create a Room."""
        view = RoomViewSet.as_view({'post': 'create'})
        building_pk = Building.objects.get().id
        data = {'building': building_pk, 'number': '247',
                'name': 'Fraternity & Sorority Life'}
        url = reverse('room-list')
        request = self.factory.post(url, data, format='json')
        force_authenticate(request, user=self.user)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Room.objects.count(), 1)
        self.assertEqual(Room.objects.get().number, '247')

    def test_room_list(self):
        """Test the api can list all the Rooms."""
        view = RoomViewSet.as_view({'get': 'list'})
        url = reverse('room-list')
        request = self.factory.get(url)
        force_authenticate(request, user=self.user)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_room_detail(self):
        """Test the api can retrieve a given Room."""
        building = Building.objects.get()
        room = Room.objects.create(building=building, number='239',
                                   name='Campus Activity Board')

        view = RoomViewSet.as_view({'get': 'retrieve'})
        url = reverse('room-detail', kwargs={'pk': room.id})
        request = self.factory.get(url)
        force_authenticate(request, user=self.user)
        response = view(request, pk=room.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_room(self):
        """Test the api can update a Room."""
        building = Building.objects.get()
        room = Room.objects.create(building=building, number='239',
                                   name='Campus Activity Board')

        view = RoomViewSet.as_view({'put': 'update'})
        data = {'building': building.id, 'number': '255',
                'name': 'Nautilus Chamber'}
        url = reverse('room-detail', kwargs={'pk': room.id})
        request = self.factory.put(url, data, format='json')
        force_authenticate(request, user=self.user)
        response = view(request, pk=room.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_room(self):
        """Test the api can delete a Room."""
        building = Building.objects.get()
        room = Room.objects.create(building=building, number='239',
                                   name='Campus Activity Board')

        view = RoomViewSet.as_view({'delete': 'destroy'})
        url = reverse('room-detail', kwargs={'pk': room.id})
        request = self.factory.delete(url)
        force_authenticate(request, user=self.user)
        response = view(request, pk=room.id)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class GroupAPITests(APITestCase):
    """Test suite for group api."""

    def setUp(self):
        self.user = User.objects.create_superuser('temp', 'temp@test.com',
                                                  'temp')
        self.client.login(username='temp', password='temp')
        self.factory = APIRequestFactory()

    def test_create_group(self):
        """Test the api can create a Group."""
        view = GroupViewSet.as_view({'post': 'create'})
        data = {'name': 'Computer Science Department'}
        url = reverse('group-list')
        request = self.factory.post(url, data, format='json')
        force_authenticate(request, user=self.user)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Group.objects.count(), 1)
        self.assertEqual(Group.objects.get().name,
                         'Computer Science Department')

    def test_group_list(self):
        """Test the api can list all the Group."""
        view = GroupViewSet.as_view({'get': 'list'})
        url = reverse('group-list')
        request = self.factory.get(url)
        force_authenticate(request, user=self.user)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_group_detail(self):
        """Test the api can retrieve a given Group."""
        group = Group.objects.create(name='Engineering Department')

        view = GroupViewSet.as_view({'get': 'retrieve'})
        url = reverse('group-detail', kwargs={'pk': group.id})
        request = self.factory.get(url)
        force_authenticate(request, user=self.user)
        response = view(request, pk=group.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_group(self):
        """Test the api can update a Group."""
        group = Group.objects.create(name='Engineering Department')

        view = GroupViewSet.as_view({'put': 'update'})
        data = {'name': 'Physics Department'}
        url = reverse('group-detail', kwargs={'pk': group.id})
        request = self.factory.put(url, data, format='json')
        force_authenticate(request, user=self.user)
        response = view(request, pk=group.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_group(self):
        """Test the api can delete a Group."""
        group = Group.objects.create(name='Engineering Department')

        view = GroupViewSet.as_view({'delete': 'destroy'})
        url = reverse('group-detail', kwargs={'pk': group.id})
        request = self.factory.delete(url, format='json', follow=True)
        force_authenticate(request, user=self.user)
        response = view(request, pk=group.id)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PersonAPITests(APITestCase):
    """Test suite for person api."""

    def setUp(self):
        self.user = User.objects.create_superuser('temp', 'temp@test.com',
                                                  'temp')
        self.client.login(username='temp', password='temp')
        self.factory = APIRequestFactory()

    def test_create_person(self):
        """Test the api can create a Person."""
        view = PersonViewSet.as_view({'post': 'create'})
        data = {'first_name': 'Bernd', 'last_name': 'Owsnicki-Klewe',
                'prefix': 'Dr'}
        url = reverse('person-list')
        request = self.factory.post(url, data, format='json')
        force_authenticate(request, user=self.user)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.get().first_name, 'Bernd')

    def test_person_list(self):
        """Test the api can list all the Person."""
        view = PersonViewSet.as_view({'get': 'list'})
        url = reverse('person-list')
        request = self.factory.get(url)
        force_authenticate(request, user=self.user)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_person_detail(self):
        """Test the api can retrieve a given Person."""
        person = Person.objects.create(first_name='John', last_name='Coffey',
                                       prefix='Dr')

        view = PersonViewSet.as_view({'get': 'retrieve'})
        url = reverse('person-detail', kwargs={'pk': person.id})
        request = self.factory.get(url)
        force_authenticate(request, user=self.user)
        response = view(request, pk=person.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_person(self):
        """Test the api can update a Person."""
        person = Person.objects.create(first_name='John', last_name='Coffey',
                                       prefix='Dr')

        view = PersonViewSet.as_view({'put': 'update'})
        data = {'first_name': 'Thomas', 'last_name': 'Reichherzer',
                'prefix': 'Dr'}
        url = reverse('person-detail', kwargs={'pk': person.id})
        request = self.factory.put(url, data, format='json')
        force_authenticate(request, user=self.user)
        response = view(request, pk=person.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_person(self):
        """Test the api can delete a Person."""
        person = Person.objects.create(first_name='John', last_name='Coffey',
                                       prefix='Dr')

        view = PersonViewSet.as_view({'delete': 'destroy'})
        url = reverse('person-detail', kwargs={'pk': person.id})
        request = self.factory.delete(url, format='json', follow=True)
        force_authenticate(request, user=self.user)
        response = view(request, pk=person.id)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
