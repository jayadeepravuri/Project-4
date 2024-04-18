from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Task(models.Model):
    """
    Model for Tasks
    """
    task_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.task_name


def validate_wednesday_date(value):
    if value.weekday() != 2:  # Wednesday is represented by the integer 2
        raise ValidationError("Volunteering date must be a Wednesday.")


class Volunteering(models.Model):
    """
    Model for Volunteering opportunities
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_volunteering"
    )
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name="task_volunteering"
    )
    date_of_volunteering = models.DateField(
        validators=[validate_wednesday_date]
    )
    confirmed = models.BooleanField(default=False)
    comments = models.TextField(max_length=500, blank=True)
    request_covolunteer = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.task.task_name} ({self.date_of_volunteering})"


class Profile(models.Model):
    """
    Model for user profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} Profile"
