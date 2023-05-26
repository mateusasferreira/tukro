from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class RegistrationTest(TestCase):

    client = APIClient()

    def test_successful_user_registration(self):
        response = self.client.post('/users/signup/', {
            'username': 'testuser',
            'password': 'Teste@123',
            'location': 'wherever',
            'email': 'test@email.com',
            'birth_date': '1995-01-01'
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)