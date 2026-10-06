from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Registration, User

def event_list(request):
    events = Event.objects.all()
    return render(
        request,
        'events/event_list.html',
        {
            'events': events
        }
    )

def event_detail(request, event_id):

    event = get_object_or_404(
        Event,
        id=event_id
    )
    registered_count = Registration.objects.filter(
        event=event,
        status='Registered'
    ).count()

    available_seats = (
        event.capacity - registered_count
    )

    return render(
        request,
        'events/event_detail.html',
        {
            'event': event,
            'registered_count': registered_count,
            'available_seats': available_seats
        }
    )

def register_event(request, event_id):

    event = get_object_or_404(
        Event,
        id=event_id
    )

    user = User.objects.first()

    existing_registration = Registration.objects.filter(
        user=user,
        event=event,
        status='Registered'
    ).first()

    if existing_registration:
        return render(
            request,
            'events/message.html',
            {
                'message': 'You are already registered for this event.'
            }
        )

    registered_count = Registration.objects.filter(
        event=event,
        status='Registered'
    ).count()

    if registered_count >= event.capacity:
        return render(
            request,
            'events/message.html',
            {
                'message': 'Event is full. Registration is closed.'
            }
        )

    Registration.objects.create(
        user=user,
        event=event,
        status='Registered'
    )

    return render(
        request,
        'events/message.html',
        {
            'message': 'Registration Successful!'
        }
    )

def my_registrations(request):

    user = User.objects.first()

    registrations = Registration.objects.filter(
        user=user
    )

    return render(
        request,
        'events/my_registrations.html',
        {
            'registrations': registrations
        }
    )

def cancel_registration(request, registration_id):

    registration = get_object_or_404(
        Registration,
        id=registration_id
    )

    registration.status = 'Cancelled'
    registration.save()

    return redirect('my_registrations')
    