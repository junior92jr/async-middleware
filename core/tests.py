from unittest.mock import patch
from django.test.client import RequestFactory

from rest_framework import status
from rest_framework.test import APITestCase

from core.models import TierAppUrl


class ApiEndpointsTestCase(APITestCase):
    """
    Test Case Main Class.
    """
    
    def setUp(self):
        self.factory = RequestFactory()
        TierAppUrl.objects.create(
            original_url='https://test2.com', 
            url_hash_string="12345678")

    def test_list_urls_200(self):
        response = self.client.get('/urls/', format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_list_urls_404(self):
        response = self.client.get('/url/', format='json')
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_create_url_201(self):
        response = self.client.post(
            '/urls/', {'original_url': 'https://test.com'}, format='json')
        
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED)
    
    def test_create_url_400_invalid_input(self):
        response = self.client.post(
            '/urls/', {'original_url': 'whatever'}, format='json')
        
        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_coallition_exception(self):
        with patch(
            'core.serializers.StoreUrlSerializer.generate_hash', 
            return_value='12345678'):

            response = self.client.post(
            '/urls/', {'original_url': 'https://test2.com'}, format='json')
            
            self.assertEqual(
                response.status_code, status.HTTP_424_FAILED_DEPENDENCY)
            
