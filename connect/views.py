from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    fields = ['task_name', 'description', 'request_covolunteer']
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')
