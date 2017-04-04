from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Building


class BuildingTests(APITestCase):
    """Tests for Building."""
    def test_create_building(self):
        url = reverse('building-list')
        data = {'number': '4',
                'name': 'Hal Marcus College of Science and Engineering'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Building.objects.count(), 1)
        self.assertEqual(Building.objects.get().number, '4')
