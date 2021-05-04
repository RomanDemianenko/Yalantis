from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from yala.api.serializers import CourseSerializer
from yala.models import Course


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def create(self, request, *args, **kwargs):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        course = get_object_or_404(Course.objects.filter(id=pk))
        serializer = CourseSerializer(instance=course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pk = self.kwargs.get('pk')
        course = get_object_or_404(Course.objects.filter(id=pk))
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        queryset = Course.objects.all()
        title = self.request.query_params.get('title', None)
        date1 = self.request.query_params.get('date1', None)
        date2 = self.request.query_params.get('date2', None)

        if title:
            queryset = queryset.filter(title__icontains=title)

        elif date1 and date2:
            q1 = Q(start__lte=date1, end__gte=date1)
            q2 = Q(start__lte=date2, end__gte=date2)
            queryset = queryset.filter(q1 | q2)

        return queryset
