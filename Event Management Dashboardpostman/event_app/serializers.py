from rest_framework import serializers
from .models import Event, Attendee, Task

# class AttendeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Attendee
#         fields = '__all__'
# class AttendeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Attendee
#         fields = ['id', 'name', 'email', 'assigned_event']
# class EventSerializer(serializers.ModelSerializer):
#     attendees = AttendeeSerializer(many=True, required=False)

#     class Meta:
#         model = Event
#         fields = '__all__'
from rest_framework import serializers
from .models import Attendee, Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'location', 'date']

class AttendeeSerializer(serializers.ModelSerializer):
    assigned_event_name = serializers.CharField(source='assigned_event.name', read_only=True)

    class Meta:
        model = Attendee
        fields = ['id', 'name', 'email', 'assigned_event', 'assigned_event_name']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'