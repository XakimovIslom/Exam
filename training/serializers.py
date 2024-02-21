from rest_framework import serializers

from training.models import Course


class CourseSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(source='owner.username')

    class Meta:
        model = Course
        fields = ('title', 'owner')
