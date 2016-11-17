from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

from model_mommy import mommy
from rest_framework.test import APITestCase, APIClient

User = get_user_model()


class ClientViewSetTest(APITestCase):
    def setUp(self):
        self.user = mommy.make(User)
        self.other_user = mommy.make(User)

        self.sample_client_object = mommy.make(
            'Client',
            name='Test Client',
            client_type='small',
            user=self.user,
        )

        other_client = mommy.make(
            'Client',
            name='Other Test Client',
            client_type='startup',
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
            self.assertEqual(client['user'], self.user.id)

    def test_get_clients_filter_by_name(self):
        name = 'Other Test Client'
        response = self.authenticated_client.get(
            reverse('client-list') + '?name=' + name
        )
        clients = response.json()

        for client in clients:
            self.assertEqual(client['name'], name)

    def test_get_clients_filter_by_client_type(self):
        client_type = 'small'
        response = self.authenticated_client.get(
            reverse('client-list') + '?client_type=' + client_type
        )
        clients = response.json()

        for client in clients:
            self.assertEqual(client['client_type'], client_type)

    def test_post_clients_returns_201(self):
        response = self.authenticated_client.post(
            reverse('client-list'),
            data=self.client_data
        )

        self.assertEqual(response.status_code, 201)

    def test_post_clients_returns_403_if_unauthenticated(self):
        response = self.client.post(
            reverse('client-list'),
            data=self.client_data
        )

        self.assertEqual(response.status_code, 403)

    def test_get_clients_returns_200_if_unauthenticated(self):
        response = self.client.get(reverse('client-list'))
        self.assertEqual(response.status_code, 403)

    def test_get_client_returns_200_if_unauthenticated(self):
        response = self.client.get(reverse('client-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 403)


class ClientContactsViewSetTest(APITestCase):
    def setUp(self):
        self.user = mommy.make(User)
        self.sample_client_object = mommy.make('Client')
        self.client_contact = mommy.make(
            'ClientContact',
            client=self.sample_client_object,
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_get_client_contacts_returns_200(self):
        response = self.client.get(reverse(
                'client-contacts-list',
                kwargs={'parent_lookup_client': self.sample_client_object.id}
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_get_client_contact_returns_200(self):
        response = self.client.get(reverse(
                'client-contacts-detail',
                kwargs={
                    'parent_lookup_client': self.sample_client_object.id,
                    'pk': self.client_contact.id
                }
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_get_client_contacts_returns_own_contacts(self):
        response = self.client.get(reverse(
                'client-contacts-list',
                kwargs={
                    'parent_lookup_client': self.sample_client_object.id
                }
            )
        )
        contacts = response.json()

        for contact in contacts:
            self.assertEqual(contact['client'], self.sample_client_object.id)

    def test_post_client_contacts_returns_201(self):
        client_contact_data = {
            'name': 'cosmo kramer',
            'email': 'a@b.com',
            'client': self.sample_client_object.id
        }
        response = self.client.post(reverse(
                'client-contacts-list',
                kwargs={
                    'parent_lookup_client': self.sample_client_object.id
                }
            ),
            data=client_contact_data
        )

        self.assertEqual(response.status_code, 201)
