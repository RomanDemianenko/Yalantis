# from unittest import TestCase
# from pytest_django.asserts import assertTemplateUsed
import json

from django.test import Client, TestCase
from django.urls import reverse

from yala.models import Course


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.course_list_url = reverse('course')
        self.detail_url = reverse('detail', args=['1'])
        self.delete_url = reverse('delete', args=['1'])
        self.course1 = Course.objects.create(title='Python', start='2021-05-12', end='2022-05-20', num_lectures=10)

    def test_course_list_get(self):
        responce = self.client.get(self.course_list_url)

        self.assertEquals(responce.status_code, 200)
        self.assertTemplateUsed(responce, 'course.html')

    def test_course_detail_get(self):
        responce = self.client.get(self.detail_url)

        self.assertEquals(responce.status_code, 200)
        self.assertTemplateUsed(responce, 'detail.html')

    def test_course_post(self):
        responce = self.client.post(reverse('create'), {
            'title': 'Java', 'start': '2021-05-20', 'end': '2022-05-27', 'num_lectures': 5})
        self.assertEquals(responce.status_code, 302)

    def test_course_delete(self):
        responce = self.client.delete(self.delete_url, json.dumps({'id': 1}))
        self.assertRedirects(responce, '/course/')

    def test_course_update(self):
        responce = self.client.post(reverse('update', kwargs={'pk': self.course1.id}),
                                   {'title': 'java', 'start': '2021-05-12', 'end': '2022-05-20', 'num_lectures': 10})
        self.assertEquals(responce.status_code, 302)

