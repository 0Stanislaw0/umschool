from django.views import generic

from lessons.models import Lesson


class UserProfileView(generic.TemplateView):
    """
    Главная страница пользователя
    """

    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context.update({"lessons": Lesson.objects.filter(users=self.request.user)})

        return context
