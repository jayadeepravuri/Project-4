from .models import Volunteering ,Task, Profile
from django import forms
from django.forms.widgets import DateInput
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime, date


class VolunteeringForm(forms.ModelForm):

    """
    Form for creating and editing haircut bookings.

    Fields:
        - date_of_booking: Date field for selecting the booking date.
        - service_name: Dropdown for selecting the haircut service.
        - start_time: Time field for selecting the booking time.
        - message: A CharField for users to enter a message.

    Widgets:
        - date_of_booking: DateInput widget with type 'date' for a date picker.

    Labels:
        - date_of_booking: 'Date'
        - service_name: 'Haircut'
        - start_time: 'Time'
        - message: 'Message'

    Custom Clean Method:
        - Ensures that the selected date and time are in the future.
        - Checks for existing bookings and raises errors if there is a clash.

    Raises:
        - ValidationError: If the selected date is not in the future.
        - ValidationError: If the selected time is not in the future.
        - ValidationError: If the selected date and time are already booked.
    """
    class Meta:
        model = Volunteering
        fields = ["date_of_volunteering", "task", 'comments', 'request_covolunteer']
        widgets = {'date_of_volunteering': DateInput(attrs={'type': 'date'}), }

        labels = {
            'date_of_volunteering': 'Date',
            'task': 'Task',
            'comments': 'Message',
            'request_covolunteer': 'Request a co-volunteer'
            }

    def clean(self):
        cleaned_data = super().clean()
        date_of_volunteering = cleaned_data.get('date_of_volunteering')
        task = cleaned_data.get('task')
        request_covolunteer =cleaned_data.get('request_covolunteer')

        if date_of_volunteering and date_of_volunteering < date.today():
            raise ValidationError('Please select a date in the future.')
            

        existing_volunteering = Volunteering.objects.filter(
            date_of_volunteering=date_of_volunteering,
            task=task,
            request_covolunteer=request_covolunteer,
        ).exclude(id=self.instance.id)
        

        if existing_volunteering:
            raise ValidationError('The task you have choosen is already taken by others.')

        if task and not task.task_name: 
            raise ValidationError('The selected task is not available.')


class VolunteeringSearchForm(forms.Form):
    """
    Form for searching bookings available in the admin panel.
    Can search for:
    - Username
    - Date of booking
    """
    search_query = forms.CharField(required=False,
                                   label='Search Username/Task')
    selected_date = forms.DateField(
        required=False,
        label='Select Date',
        widget=forms.DateInput(attrs={'type': 'date'}),
    )



class UserUpdateForm(forms.ModelForm):
    """
    Form for profile name update
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


