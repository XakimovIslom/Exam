from rest_framework import generics

from training.models import Course
from training.serializers import CourseSerializer


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
