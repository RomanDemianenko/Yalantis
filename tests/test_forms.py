import datetime
from unittest import TestCase

from yala.forms import CourseForm


class CourseFormTest(TestCase):

    def test_form(self):
        end = datetime.date.today() - datetime.timedelta(days=1)
        start = datetime.date.today()
        form_data = {'start': start, 'end': end}
        form = CourseForm(data=form_data)
        self.assertFalse(form.is_valid())
