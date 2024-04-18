from . import views
from django.urls import path


urlpatterns = [
    path("volunteer/", views.VolunteeringListView.as_view(), name="volunteer-home"),
    path("profile", views.profile_view, name="profile"),
    path(
        "volunteer/create", views.CreateVolunteerView.as_view(), name="volunteer-create"
    ),
    path(
        "volunteer/<int:pk>/",
        views.VolunteeringDetailView.as_view(),
        name="volunteer-detail",
    ),
    path(
        "volunteer/<int:pk>/update/",
        views.UpdateVolunteeringView.as_view(),
        name="volunteer-update",
    ),
    path(
        "volunteer/<int:pk>/delete/",
        views.VolunteeringDeleteView.as_view(),
        name="volunteer-delete",
    ),
    path(
        "volunteer/<int:pk>/confirm/",
        views.ConfirmVolunteeringView.as_view(),
        name="confirm-volunteer",
    ),
]
