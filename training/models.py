from django.contrib.auth.models import User
from django.db import models

from common.models import BaseModel


class Course(BaseModel):
    title = models.CharField(max_length=256)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')

    def __str__(self):
        return self.title


class Lesson(BaseModel):
    title = models.CharField(max_length=256)
    course = models.ManyToManyField(Course, related_name='lessons')
    video_link = models.CharField(max_length=256)
    total_time = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class LessonUser(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    time_watched = models.IntegerField(default=0)
    total_time = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user} - {self.lesson}"

    def is_finished(self):
        return self.total_time * 0.8 <= self.time_watched

    @property
    def status(self):
        if self.is_finished():
            return "Ko`rilgan"
        return "Ko`rilmagan"


class LessonUserWatched(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(LessonUser, on_delete=models.CASCADE)

    from_time = models.IntegerField(default=0)
    to_time = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user} - {self.lesson}"

