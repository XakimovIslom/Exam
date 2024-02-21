from django.contrib import admin

from training.models import Course, Lesson, LessonUser, LessonUserWatched

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(LessonUser)
admin.site.register(LessonUserWatched)
