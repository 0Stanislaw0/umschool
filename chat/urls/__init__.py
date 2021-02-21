from django.urls import path

from chat.views.lesson import LessonDetailView

app_name = "chat"

urlpatterns = [path("<pk>/", LessonDetailView.as_view(), name="room")]
