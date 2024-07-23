from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from teleafya.models import teleafya

# Create your tests here

class teleafyaAPITestCase(APITestCase):
    def create_teleafya(self):
        sample_teleafya = {'title': "Hello", "desc": "Test"}
        response = self.client.post(reverse('teleafya'), sample_teleafya)

        return response

    def authenticate(self):
        self.client.post(reverse('register'), {
            'username': "username", "email":"email@gmail.com", "password": "password"
        })

        response = self.client.post(reverse('login'), {"email":"email@gmail.com", "password": "password"})

        self.client.credentials(
                HTTP_AUTHORIZATION=f"Bearer {response.data['token']}"
        )

class TestListCreateteleafya(teleafyaAPITestCase):

    def test_should_not_create_teleafya_with_no_auth(self):
        
        response = self.create_teleafya()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_should_create_teleafya(self):
        previous_teleafya_count = teleafya.objects.all().count()
        self.authenticate()
        response = self.create_teleafya()
        self.assertEqual(teleafya.objects.all().count(), previous_teleafya_count+1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Hello')
        self.assertEqual(response.data['desc'], 'Test')

    def test_retrieves_all_teleafya(self):
        self.authenticate()
        response = self.client.get(reverse('teleafya'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['results'], list)

        self.create_teleafya()
        res = self.client.get(reverse('teleafya'))
        self.assertIsInstance(response.data['count'], int)
        self.assertEqual(res.data['count'], 1)

class TestteleafyaDetailAPIView(teleafyaAPITestCase):
    
    def test_retrieves_one_item(self):
        self.authenticate()
        response = self.create_teleafya()

        res=self.client.get(reverse("teleafya", kwargs={'id': response.data['id']}))

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        t_eleafya = teleafya.objects.get(id=response.data['id'])

        self.assertEqual(t_eleafya.title, res.data['title'])

    def test_updates_one_item(self):
        self.authenticate()
        response = self.create_teleafya()

        res = self.client.patch(
            reverse("teleafya", kwargs={'id': response.data['id']}), {
                "title": "New one", 'is_complete': True
            })
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        updated_teleafya = teleafya.objects.get(id=response.data['id'])

        self.assertEqual(updated_teleafya.is_complete, True)

    def test_deletes_one_item(self):
        self.authenticate()
        res = self.create_teleafya()
        prev_db_count = teleafya.objects.all().count()

        self.assertGreater(prev_db_count, 0)
        self.assertEqual(prev_db_count, 1)

        response = self.client.delete(reverse("teleafya", kwargs={'id': res.data['id']}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(teleafya.objects.all().count(), 0)


