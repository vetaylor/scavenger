from django.test import TestCase

from rest_framework.test import APIRequestFactory

factory = APIRequestFactory()
request = factory.post(
    '/buildings/', {'number': '4',
                    'name': 'Hal Marcus College of Science and Engineering'},
    format='json')
