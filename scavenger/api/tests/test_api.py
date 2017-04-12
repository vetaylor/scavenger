from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, \
                                force_authenticate

from scavenger.api.models import Building
from scavenger.api.views import BuildingViewSet


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
