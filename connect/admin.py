from django.contrib import admin
from .models import Task, Volunteering

# Register your models here.
@admin.register(Volunteering)
class VolunteeringAdmin(admin.ModelAdmin):
        list_display = ('user',
                         'date_of_volunteering',
                         'task',
                         'confirmed')
        list_filter = ('date_of_volunteering', 'user')
        search_feilds = ['username', 'task']
        actions = ['confirm_booking']

        def confirm_booking(self, request, queryset):
            queryset.update(confirmed=true)


@admin.register(Task)
class VolunteeringTask(admin.ModelAdmin):
    list_display = ('task_name','description', 'request_covolunteer')
