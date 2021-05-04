from django import forms

from yala.models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def clean(self):
        end = self.cleaned_data.get('end')
        start = self.cleaned_data.get('start')
        if end <= start:
            raise forms.ValidationError("You have to change the date")

        return self.cleaned_data
