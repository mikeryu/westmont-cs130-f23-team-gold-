from django.urls import path
<<<<<<< HEAD


=======
>>>>>>> 5de198d (view event details  (#56))
from . import views

app_name = "planner"
urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("event_creation/", views.event_creation, name="event_creation"),
    path("<int:event_id>/edit_event/", views.edit_event, name="edit_event"),
    path('event/<int:event_id>/', views.event_home, name='event_home'),
    path("<int:event_id>/invitations/", views.invitations, name="invitations"),
    path('addRoles/', views.addRoles, name="addRoles")
]
