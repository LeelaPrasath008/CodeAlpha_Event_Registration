# Event Registration System

A Django-based Event Registration System that allows users to browse events, register for events, manage registrations, and track event capacity.

## Features

- View all available events
- View detailed event information
- Register for events
- Prevent duplicate registrations
- Event capacity validation
- Available seat tracking
- Cancel registrations
- Registration status management
- Django Admin Panel
- Responsive Bootstrap UI

## Tech Stack

- Python 3.14
- Django 6.1.1
- SQLite
- Bootstrap 5

## Database Models

### Event
- Title
- Description
- Date
- Location
- Organizer
- Capacity

### Registration
- User
- Event
- Status

## Project Structure

```text
events/
event_registration/
manage.py
requirements.txt
```

## Installation

```bash
git clone <repository-url>
cd CodeAlpha_Event_Registration

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

## Learning Outcomes

- Django Models
- Django ORM
- Migrations
- Templates
- URL Routing
- Bootstrap UI Design
- Database Relationships
- Validation Logic

## Author

Leelaprasath V