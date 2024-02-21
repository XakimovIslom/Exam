from rest_framework import serializers

from training.models import Course, Lesson, LessonUser


class LessonUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonUser
        fields = ('status', 'time_watched')


class LessonSerializer(serializers.ModelSerializer):
    # course = serializers.StringRelatedField(source='course.title')

    class Meta:
        model = Lesson
        fields = ('title', 'course', 'video_link', 'total_time')


class CourseSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(source='owner.username')
    lessons = LessonSerializer(many=True, read_only=True)
    # lesson_user = LessonUserSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('title', 'owner', 'lessons', 'lesson_user')
