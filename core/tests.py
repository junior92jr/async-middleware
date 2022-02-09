import unittest

from unittest.mock import patch
from django.test.client import RequestFactory

from rest_framework import status
from rest_framework.test import APITestCase

from core.models import TierAppUrl
from core.views import TierAppUrlViewset
from core.exceptions import RepeatedUrlHashException


class ApiEndpointsTestCase(APITestCase):
    def setUp(self):
        self.factory = RequestFactory()
        TierAppUrl.objects.create(
            original_url="https://test2.com", 
            url_hash_string="12345678")

    def test_list_urls_200(self):
        response = self.client.get('/urls/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_url_201(self):
        response = self.client.post(
            '/urls/', {'original_url': 'https://test.com'}, format='json')
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED)
    
    def test_create_url_400(self):
        response = self.client.post(
            '/urls/', {'original_url': 'whatever'}, format='json')
        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST)

    # @unittest.expectedFailure
    def test_coallition_exception(self):
        with patch(
            'core.serializers.StoreUrlSerializer.generate_hash', 
            return_value='12345678'):
            with self.assertRaises(RepeatedUrlHashException):
                request = self.factory.post('/urls/')
                request.data = {'original_url': 'https://test2.com'}
                TierAppUrlViewset().create(request)
