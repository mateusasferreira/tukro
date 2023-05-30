from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from users.models import User


class RegistrationTest(TestCase):

    client = APIClient()

    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.user_taken = User.objects.create_user(
            username= 'existinguser',
            password= 'Teste@123',
            location= 'wherever',
            email= 'testexisting@email.com',
            birth_date= '1995-01-01'
        )

    def test_successful_user_registration(self):
        payload = {
            'username': 'testuser',
            'password': 'Teste@123',
            'location': 'wherever',
            'email': 'test@email.com',
            'birth_date': '1995-01-01'
        }

        response = self.client.post('/users/signup/', payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_username_taken_bad_request(self):
        response = self.client.post('/users/signup/', {
            'username': 'existinguser',
            'password': 'Teste@123',
            'location': 'wherever',
            'email': 'test2@email.com',
            'birth_date': '1995-01-01'
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_week_password_bad_request(self):
        response = self.client.post('/users/signup/', {
            'username': 'testeuser2',
            'password': 'teste',
            'location': 'wherever',
            'email': 'test3@email.com',
            'birth_date': '1995-01-01'
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_no_location_bad_request(self):
        response = self.client.post('/users/signup/', {
            'username': 'testeuser3',
            'password': 'Teste@123',
            'email': 'test4@email.com',
            'birth_date': '1995-01-01'
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_no_birth_date_bad_request(self):
        response = self.client.post('/users/signup/', {
            'username': 'testeuser4',
            'password': 'Teste@123',
            'location': 'wherever',
            'email': 'test5@email.com',
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)