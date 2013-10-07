from django.utils import unittest
from django.test.client import Client
from django.contrib.auth.models import User
from achievement.models import Achievement

class AhievementTest(unittest.TestCase):
    def setUp(self):
        self.user, is_new = User.objects.get_or_create(username = 'panga')
        if is_new:
            self.user.set_password('parola')
            self.user.save()
        self.client = Client().post('/login', {'username': 'panga', 'password': 'parola'}).client

    def test_basic(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
