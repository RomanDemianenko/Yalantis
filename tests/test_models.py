from django.test import TestCase

from yala.models import Course


class CourseModelTest(TestCase):

    def setUp(self):
        self.course = Course.objects.create(title='PhP', start='2021-05-12', end='2022-05-20', num_lectures=10)

    def test_title_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('title').max_length
        self.assertEquals(max_length, 20)

    def test_num_lectures(self):
        course = Course.objects.get(id=1)
        num_lectures = course._meta.get_field('num_lectures')
        self.assertNotEqual(num_lectures, 0)
