from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

from model_mommy import mommy
from rest_framework.test import APITestCase, APIClient


class APITests(APITestCase):
    def setUp(self):
        self.user = mommy.make('User')
        self.other_user = mommy.make('User')

        self.sample_client_object = mommy.make(
            'Client',
            name='Test Person',
            user=self.user,
        )

        other_client = mommy.make(
            'Client',
            name='Test Person',
            user=self.other_user,
        )

        self.client_data = {
            'name': 'other test person',
            'client_type': 'small',
            'user': self.user.id
        }

        self.client = APIClient()
        self.authenticated_client = APIClient()
        self.authenticated_client.force_authenticate(user=self.user)

    def test_get_clients_returns_200(self):
        response = self.authenticated_client.get(reverse('client-list'))
        self.assertEqual(response.status_code, 200)

    def test_get_client_returns_200(self):
        response = self.authenticated_client.get(
            reverse(
                'client-detail',
                kwargs={'pk': self.sample_client_object.pk}
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_get_clients_returns_own_data(self):
        response = self.authenticated_client.get(reverse('client-list'))
        clients = response.json()

        for client in clients:
            self.assertEqual(client['id'], self.user.id)

    def test_post_clients_returns_data(self):
        response = self.authenticated_client.post(
            reverse('client-list'),
            data=self.client_data
        )

        self.assertEqual(response.status_code, 201)

    def test_unauthenticated_client_cant_post_data(self):
        response = self.client.post(
            reverse('client-list'),
            data=self.client_data
        )

        self.assertEqual(response.status_code, 403)

    def test_unauthenticated_client_cant_get_one(self):
        response = self.client.get(reverse('client-list'))
        self.assertEqual(response.status_code, 403)

    def test_unauthenticated_client_cant_get_list(self):
        response = self.client.get(reverse('client-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 403)

