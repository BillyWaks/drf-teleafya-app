from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from appointments.models import appointments

# Create your tests here

class appointmentsAPITestCase(APITestCase):
    def create_appointments(self):
        sample_appointments = {'title': "Hello", "desc": "Test"}
        response = self.client.post(reverse('appointments'), sample_appointments)

        return response

    def authenticate(self):
        self.client.post(reverse('register'), {
            'username': "username", "email":"email@gmail.com", "password": "password"
        })

        response = self.client.post(reverse('login'), {"email":"email@gmail.com", "password": "password"})

        self.client.credentials(
                HTTP_AUTHORIZATION=f"Bearer {response.data['token']}"
        )

class TestListCreateappointments(appointmentsAPITestCase):

    def test_should_not_create_appointments_with_no_auth(self):
        
        response = self.create_appointments()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_should_create_appointments(self):
        previous_appointments_count = appointments.objects.all().count()
        self.authenticate()
        response = self.create_appointments()
        self.assertEqual(appointments.objects.all().count(), previous_appointments_count+1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Hello')
        self.assertEqual(response.data['desc'], 'Test')

    def test_retrieves_all_appointments(self):
        self.authenticate()
        response = self.client.get(reverse('appointments'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['results'], list)

        self.create_appointments()
        res = self.client.get(reverse('appointments'))
        self.assertIsInstance(response.data['count'], int)
        self.assertEqual(res.data['count'], 1)

class TestappointmentsDetailAPIView(appointmentsAPITestCase):
    
    def test_retrieves_one_item(self):
        self.authenticate()
        response = self.create_appointments()

        res=self.client.get(reverse("appointments", kwargs={'id': response.data['id']}))

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        t_eleafya = appointments.objects.get(id=response.data['id'])

        self.assertEqual(t_eleafya.title, res.data['title'])

    def test_updates_one_item(self):
        self.authenticate()
        response = self.create_appointments()

        res = self.client.patch(
            reverse("appointments", kwargs={'id': response.data['id']}), {
                "title": "New one", 'is_complete': True
            })
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        updated_appointments = appointments.objects.get(id=response.data['id'])

        self.assertEqual(updated_appointments.is_complete, True)

    def test_deletes_one_item(self):
        self.authenticate()
        res = self.create_appointments()
        prev_db_count = appointments.objects.all().count()

        self.assertGreater(prev_db_count, 0)
        self.assertEqual(prev_db_count, 1)

        response = self.client.delete(reverse("appointments", kwargs={'id': res.data['id']}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(appointments.objects.all().count(), 0)


