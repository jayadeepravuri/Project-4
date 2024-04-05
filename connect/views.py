from django.urls import reverse_lazy
from django.http  import HttpResponse
from .models import Task , Volunteering
from django.views.generic import CreateView , ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from datetime import date
import time

def my_connect(request):
 return HttpResponse("Hello, there!")


class TaskList( ListView):
    model = Task
    template_name = 'connect/index.html'
    paginate_by = 25




    