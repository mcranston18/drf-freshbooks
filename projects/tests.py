from datetime import date

from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from model_mommy import mommy

from rest_framework.test import APITestCase, APIClient

User = get_user_model()


class APITests(APITestCase):
    def setUp(self):
        self.user = mommy.make(User)

        sample_client_object = mommy.make(
            'Client',
            user=self.user
        )

        self.other_sample_client_object = mommy.make(
            'Client',
            user=self.user
        )

        self.project = mommy.make(
            'Project',
            client=sample_client_object,
            budget=1000,
            status='active'
        )

        self.other_project = mommy.make(
            'Project',
            client=self.other_sample_client_object,
            budget=100000,
            status='inactive',
        )

        self.project_data = {
            'budget': 1000,
            'client': sample_client_object.id,
            'title': 'some title',
            'description': 'description',
            'start_date': date.today(),
            'status': 'active',
        }

        self.client = APIClient()
        self.authenticated_client = APIClient()
        self.authenticated_client.force_authenticate(user=self.user)

    def test_get_projects_returns_200(self):
        response = self.authenticated_client.get(reverse('project-list'))
        self.assertEqual(response.status_code, 200)

    def test_get_project_returns_200(self):
        response = self.authenticated_client.get(
            reverse(
                'project-detail',
                kwargs={'pk': self.project.pk}
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_get_products_filter_by_client(self):
        client_id = self.other_sample_client_object.id
        response = self.authenticated_client.get(
            reverse('project-list') + '?client=%s' % client_id
        )
        projects = response.json()


        for project in projects:
            self.assertEqual(project['client'], client_id)

    def test_get_products_filter_by_status(self):
        status = 'active'
        response = self.authenticated_client.get(
            reverse('project-list') + '?status=%s' % status
        )
        projects = response.json()


        for project in projects:
            self.assertEqual(project['status'], status)

    def test_get_products_filter_by_min_budget(self):
        min_budget = 10000
        response = self.authenticated_client.get(
            reverse('project-list') + '?min_budget=%s' % min_budget
        )
        projects = response.json()


        for project in projects:
            self.assertTrue(project['budget'] > min_budget)

    def test_get_products_filter_by_max_budget(self):
        max_budget = 10000
        response = self.authenticated_client.get(
            reverse('project-list') + '?max_budget=%s' % max_budget
        )
        projects = response.json()


        for project in projects:
            self.assertTrue(project['budget'] < max_budget)

    def test_post_projects_returns_201(self):
        response = self.authenticated_client.post(
            reverse('project-list'),
            data=self.project_data
        )

        self.assertEqual(response.status_code, 201)

    def test_post_projects_returns_403_if_unauthenticated(self):
        response = self.client.post(
            reverse('project-list'),
            data=self.project_data
        )

        self.assertEqual(response.status_code, 403)

    def test_get_projects_returns_200_if_unauthenticated(self):
        response = self.client.get(reverse('project-list'))
        self.assertEqual(response.status_code, 403)

    def test_get_project_returns_200_if_unauthenticated(self):
        response = self.client.get(reverse('project-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 403)


