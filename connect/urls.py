from . import views
from django.urls import path
from .views import (TaskList)

urlpatterns = [
    path("",views.TaskList.as_view(), name="home")
]