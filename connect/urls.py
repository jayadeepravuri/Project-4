from . import views
from django.urls import path

urlpatterns = [
    path('', views.TaskListView.as_view(),
         name='task-home'),
]