from django.test import TestCase, Client
from rest_framework.test import APIClient
from .models import User


class LoginTestCase(TestCase):

    def setUp(self):
        self.username = "Daniyar"
        self.password = "test123"
        self.user = User.objects.create_user(username=self.username, password=self.password)

        # Log in the client
        self.client = Client()
        self.client.login(username=self.username, password=self.password)

        self.content_type = "application/json"


    def test_user_info(self):
        response = self.client.get('/en/api/user/info/', content_type=self.content_type)
        self.assertEqual(response.status_code, 200)