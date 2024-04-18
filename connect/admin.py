from django.contrib import admin
from .models import Task, Volunteering


# Register your models here.
@admin.register(Volunteering)
class VolunteeringAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "date_of_volunteering",
        "task",
        "confirmed",
        "request_covolunteer",
    )
    list_filter = ("date_of_volunteering", "user")
    search_feilds = ["username", "task"]
    actions = ["confirm_volunteer"]

    def confirm_booking(self, request, queryset):
        queryset.update(confirmed=True)


@admin.register(Task)
class VolunteeringTask(admin.ModelAdmin):
    list_display = (
        "task_name",
        "description",
    )
