from django.views import generic

from chat.models import Message
from lessons.models import Lesson


class LessonDetailView(generic.DetailView):
    queryset = Lesson.objects.all()
    template_name = "chat/room.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context.update(
            {
                "messages": Message.objects.filter(lesson_id=self.object.id).order_by(
                    "-created_at"
                )[:10]
            }
        )

        return context
