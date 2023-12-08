from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from  apps.users.models import User


class RegistrationTest(TestCase):

    client = APIClient()

    @classmethod
    def setUpTestData(cls):
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
        self.assertTrue("username" in response.data["errors"])

    def test_email_taken_bad_request(self):
        response = self.client.post('/users/signup/', {
            'username': 'emailtakenuser',
            'password': 'Teste@123',
            'location': 'wherever',
            'email': 'testexisting@email.com',
            'birth_date': '1995-01-01'
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("email" in response.data["errors"])

    def test_week_password_bad_request(self):
        response = self.client.post('/users/signup/', {
            'username': 'testeuser',
            'password': 'soweak',
            'location': 'wherever',
            'email': 'test@email.com',
            'birth_date': '1995-01-01'
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("password" in response.data["errors"])

    def test_no_location_bad_request(self):
        response = self.client.post('/users/signup/', {
            'username': 'testeuser',
            'password': 'Teste@123',
            'email': 'test@email.com',
            'birth_date': '1995-01-01'
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("location" in response.data["errors"])

    def test_no_birth_date_bad_request(self):
        response = self.client.post('/users/signup/', {
            'username': 'testeuser',
            'password': 'Teste@123',
            'location': 'wherever',
            'email': 'test@email.com',
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("birth_date" in response.data["errors"])