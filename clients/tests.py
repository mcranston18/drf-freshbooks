from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase, APIClient

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

        print('hey!!')

        self.client_data = {
            'name': 'other test person',
            'client_type': 'small',
            'user': str(self.user.id)
        }

        self.client = APIClient()
        self.authenticated_client = APIClient()
        self.authenticated_client.force_authenticate(user=self.user)

    def test_get_clients_returns_data(self):
        response = self.authenticated_client.get(reverse('client-list'))
        self.assertEqual(response.status_code, 200)

    def test_get_client_returns_data(self):
        response = self.authenticated_client.get(reverse('client-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_post_clients_returns_data(self):
        response = self.authenticated_client.post(
            reverse('client-list'),
            data=self.client_data
        )
        print(self.client_data)

        self.assertEqual(response.status_code, '201')

    def test_unauthenticated_clients_cant_get_data(self):
        response = self.client.get(reverse('client-list'))
        self.assertEqual(response.status_code, 403)

    def test_unauthenticated_client_cant_get_data(self):
        response = self.client.get(reverse('client-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 403)

