from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    organizer = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Registration(models.Model):

    STATUS_CHOICES = [
        ('Registered', 'Registered'),
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )

    registered_at = models.DateTimeField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Registered'
    )

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"