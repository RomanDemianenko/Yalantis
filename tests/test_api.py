from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
import json

from yala.api.serializers import CourseSerializer
from yala.models import Course


class CourseViewSetTest(APITestCase):

    def setUp(self):
        self.course1 = Course.objects.create(title='Python', start='2021-05-12', end='2022-05-20', num_lectures=10)
        self.course2 = Course.objects.create(title='Java', start='2021-05-10', end='2022-05-13', num_lectures=3)
        # self.client = APIClient()

    def test_get_data(self):
        data = {'id': 2, 'title': 'Java', 'start': '2021-05-10', 'end': '2022-05-13', 'num_lectures': 3}
        response = self.client.get(reverse('course-detail', kwargs={'pk': 2}))
        self.assertEqual(response.data, data)

    def test_create_course(self):
        course = {
            'title': 'hello', 'start': '2021-04-20', 'end': '2021-05-01', 'num_lectures': 20
        }
        response = self.client.post(reverse('course-list'), data=json.dumps(course),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update(self):
        course = {'title': 'java', 'start': '2021-05-12', 'end': '2022-05-20', 'num_lectures': 10}
        responce = self.client.put(reverse('course-detail', kwargs={'pk': 2}), data=json.dumps(course),
                                   content_type='application/json')
        self.assertEqual(responce.status_code, status.HTTP_200_OK)

    def test_update_invalid(self):
        course = {'title': 'java', 'start': '2021-05-12', 'end': '2022-05-20', 'num_lectures': 10}
        responce = self.client.put(reverse('course-detail', kwargs={'pk': 30}), data=json.dumps(course),
                                   content_type='application/json')
        self.assertEqual(responce.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete(self):
        responce = self.client.delete(reverse('course-detail', kwargs={'pk': 1}))
        self.assertEqual(responce.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid(self):
        responce = self.client.delete(reverse('course-detail', kwargs={'pk': 30}))
        self.assertEqual(responce.status_code, status.HTTP_404_NOT_FOUND)
