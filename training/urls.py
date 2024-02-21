from django.urls import path
from training import views

urlpatterns = [
    path('', views.CourseListAPIView.as_view()),
]