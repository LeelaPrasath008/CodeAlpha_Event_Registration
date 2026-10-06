from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),

    path(
        '<int:event_id>/',
        views.event_detail,
        name='event_detail'
    ),
    path(
        'register/<int:event_id>/',
        views.register_event,
        name='register_event'
    ),
    path(
        'my-registrations/',
        views.my_registrations,
        name='my_registrations'
    ),
    path(
        'cancel/<int:registration_id>/',
        views.cancel_registration,
        name='cancel_registration'
    ),
]