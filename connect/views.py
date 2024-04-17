from django.urls import reverse_lazy
from django.db.models import Q
from django.http  import HttpResponse
from .models import Volunteering, Task, Profile
from .forms import VolunteeringForm, VolunteeringSearchForm, UserUpdateForm
from django.views.generic import (CreateView ,ListView,DetailView,UpdateView,
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date
from django.shortcuts import (
    render, get_object_or_404, reverse, redirect, resolve_url)


class VolunteeringListView(LoginRequiredMixin,ListView):
    model = Volunteering
    template_name = 'connect/volunteer_home.html'
    paginate_by =6
    form_class = VolunteeringSearchForm

    def get_queryset(self):
        current_date = date.today()
        form = VolunteeringSearchForm(self.request.GET)

        if self.request.user.is_superuser:
            if form.is_valid():
                search_query = form.cleaned_data['search_query']
                selected_date = form.cleaned_data['selected_date']
                queryset = Volunteering.objects.filter(
                    Q(date_of_volunteering__gt=current_date) |
                    Q(date_of_volunteering=current_date),
                    Q(user__username__icontains=search_query) |
                    Q(task__task_name__icontains=search_query),
                    Q(date_of_volunteering=selected_date) if selected_date else Q()
                ).order_by('date_of_volunteering')
        else:
            queryset = Volunteering.objects.filter(
                user = self.request.user).filter(
                    Q(date_of_volunteering__gt=current_date)
                ).order_by('date_of_volunteering')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = VolunteeringSearchForm()
        return context

class CreateVolunteerView(LoginRequiredMixin, CreateView):
    """
    View for creating a new booking.

    Attributes:
        - model: Booking from models.py
        - template_name: The path to the template for rendering the view.
        - success_url: Redirects to booking-home after a successful form.
        - form_class: The form class to use for creating a new booking.

    Methods:
        - form_valid(form): Overrides the form_valid method.
        Sets the username and calculates the end time
        and sends a confirmation email
        and alerts the user of a successful booking.
    """
    model = Volunteering
    template_name = 'connect/volunteer_form.html'
    success_url = reverse_lazy('volunteer-home')
    form_class = VolunteeringForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request,"Your task has been successfully created!",
            extra_tags="alert alert-success alert-dismissible",)
        return super().form_valid(form)



class UpdateVolunteeringView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View for updating an existing booking.

    Attributes:
        - model: Booking from models.py
        - template_name: The path to the template for rendering the view.
        - success_url: Redirect to booking-home after a successful form.
        - form_class: The form class to use for updating a booking.

    Methods:
        - form_valid(form): Overrides the form_valid method for customization.
        Calculates the end time after a successful form submission and sends a
        confirmation email to the user.

        - test_func(): Checks if the current user is allowed to update the
        booking.
        Users that created the booking and admins have the ability to update.
    """
    model = Volunteering
    template_name = 'connect/volunteer_form.html'
    success_url = reverse_lazy('volunteer-home')
    form_class = VolunteeringForm

    def form_valid(self, form):
        form.instance.confirmed = False
        messages.success(
            self.request,
            "Your Task has been successfully updated!",
            extra_tags="alert alert-success alert-dismissible",
        )
        return super().form_valid(form)
    

    def test_func(self):
        volunteering = self.get_object()
        return (self.request.user == volunteering.user or
                self.request.user.is_superuser)

class VolunteeringDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):

    model = Volunteering

    def test_func(self):
        volunteering = self.get_object()
        return (self.request.user == volunteering.user or
                self.request.user.is_superuser)

class VolunteeringDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Volunteering
    success_url = reverse_lazy('volunteer-home')

    def delete(self, request, *args, **kwargs):
        volunteering = self.get_object()
        messages.success(
            self.request,
            "Your Task has been successfully deleted!",
            extra_tags="alert alert-danger alert-dismissible",
        )
        return super().delete(request, *args, **kwargs)

    def test_func(self):
        volunteering = self.get_object()
        return (self.request.user == volunteering.user or
                self.request.user.is_superuser)

class ConfirmVolunteeringView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Volunteering
    fields = ['confirmed']
    success_url = reverse_lazy('volunteer-home')

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        form.instance.confirmed = True
        form.save()

        messages.success(self.request,
                         "The volunteering has been confirmed!",
                         extra_tags="alert alert-success alert-dismissible",
                         )
        return super().form_valid(form)


def profile_view(request):
    """
    Renders the profile page
    """
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)

    context = {
        'user_form': user_form,
    }
    return render(request, 'connect/profile.html', context)
    