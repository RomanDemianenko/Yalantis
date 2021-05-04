from rest_framework import serializers

from yala.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    def validate(self, data):
        end = data['end']
        start = data['start']
        if end < start:
            raise serializers.ValidationError("You should mix up date")
        return data