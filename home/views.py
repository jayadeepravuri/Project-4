from django.views.generic import TemplateView
from connect.models import Task


class HomeView(TemplateView):
    """
    View to render the landing page.

    Attributes:
        - template_name: home/index.html
    """

    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = Task.objects.all()
        return context
