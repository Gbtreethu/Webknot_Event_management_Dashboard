from django.db import models

# class Event(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     location = models.CharField(max_length=200)
#     date = models.DateField()
#     attendees = models.ManyToManyField('Attendee', related_name='events', blank=True)

#     def __str__(self):
#         return self.name

# class Attendee(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     assigned_event = models.ForeignKey(Event, null=True, blank=True, on_delete=models.SET_NULL, related_name='assigned_attendees')

#     def __str__(self):
#         return self.name
from django.db import models
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateField()
    attendees = models.ManyToManyField('Attendee', related_name='events', blank=True)

    def __str__(self):
        return self.name

class Attendee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    assigned_event = models.ForeignKey(
        Event, null=True, blank=True, on_delete=models.SET_NULL, related_name='assigned_attendees'
    )

    def __str__(self):
        return self.name
# class Event(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     location = models.CharField(max_length=200)
#     date = models.DateField()
#     attendees = models.ManyToManyField('Attendee', related_name='events', blank=True)

#     def __str__(self):
#         return self.name

# class Attendee(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     assigned_event = models.ForeignKey(
#         Event, null=True, blank=True, on_delete=models.SET_NULL, related_name='assigned_attendees'
#     )

#     def __str__(self):
#         return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]

    name = models.CharField(max_length=100)
    deadline = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    event = models.ForeignKey(Event, related_name='tasks', on_delete=models.CASCADE)
    assigned_attendee = models.ForeignKey(Attendee, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name