from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase

from clients.models import Client


User = get_user_model()


class APITests(APITestCase):
    def setUp(self):
        self.user = User(username='testuser', password='pass')
        self.user.save()


        client = Client(
            name='Test Person',
            client_type='startup',
            user=self.user)
        client.save()

        self.client_data = {
            'name': 'other test person',
            'client_type': 'small',
            'user': 1
        }


    def test_get_clients(self):
        response = self.client.get(reverse('client-list'))
        self.assertEqual(response.status_code, 200)

    def test_get_client(self):
        response = self.client.get(reverse('client-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)


