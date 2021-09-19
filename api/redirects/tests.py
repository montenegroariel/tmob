from django.shortcuts import redirect
from django.test import TestCase
from django.urls.base import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Redirect
from .views import RedirectViewSet
from rest_framework.test import APIRequestFactory
from django.contrib.auth.models import User

class RedirectAPITestCase(APITestCase):

    def setUp(self) -> None:
        redirect = Redirect(key='s2',url='https://www.seostax.com')
        redirect.save()
        return super().setUp()
    
    def test_create_redirect(self):
        user = User.objects.create_user("admin" "admin@test.com", "Pass.1234")
        self.client.force_login(user=user)
        response = self.client.post(
                '/redirects/', {
                'key': 's1',
                'url': 'https://www.google.com',
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_perms_create_redirect(self):

        response = self.client.post(
                '/redirects/', {
                'key': 's1',
                'url': 'https://www.google.com',
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
     
    def test_get_url(self):
        user = User.objects.create_user("admin" "admin@test.com", "Pass.1234")
        self.client.force_login(user=user)
        response = self.client.get(
                '/redirects/', {
                'key': 's2',
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_perms_get_url(self):

            response = self.client.get(
                    '/redirects/', {
                    'key': 's2',
                },
                format='json'
            )
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)