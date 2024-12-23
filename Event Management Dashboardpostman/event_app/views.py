# # views.py
# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Event, Attendee, Task
# from .serializers import EventSerializer, AttendeeSerializer, TaskSerializer

# from django.shortcuts import render

# def index(request):
#     return render(request, 'index.html')
# # Event Management API
# class EventViewSet(viewsets.ViewSet):
#     def create(self, request):
#         serializer = EventSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def list(self, request):
#         events = Event.objects.all()
#         serializer = EventSerializer(events, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         try:
#             event = Event.objects.get(pk=pk)
#             serializer = EventSerializer(event)
#             return Response(serializer.data)
#         except Event.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def update(self, request, pk=None):
#         try:
#             event = Event.objects.get(pk=pk)
#             serializer = EventSerializer(event, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Event.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def destroy(self, request, pk=None):
#         try:
#             event = Event.objects.get(pk=pk)
#             event.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Event.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

# # Attendee Management API
# class AttendeeViewSet(viewsets.ViewSet):
#     def create(self, request):
#         serializer = AttendeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def list(self, request):
#         attendees = Attendee.objects.all()
#         serializer = AttendeeSerializer(attendees, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         try:
#             attendee = Attendee.objects.get(pk=pk)
#             serializer = AttendeeSerializer(attendee)
#             return Response(serializer.data)
#         except Attendee.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def destroy(self, request, pk=None):
#         try:
#             attendee = Attendee.objects.get(pk=pk)
#             attendee.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Attendee.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

# # Task Management API
# class TaskViewSet(viewsets.ViewSet):
#     def create(self, request):
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def list(self, request):
#         event_id = request.query_params.get('event_id', None)
#         if event_id is not None:
#             tasks = Task.objects.filter(event_id=event_id)
#         else:
#             tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         try:
#             task = Task.objects.get(pk=pk)
#             serializer = TaskSerializer(task)
#             return Response(serializer.data)
#         except Task.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def update(self, request, pk=None):
#         try:
#             task = Task.objects.get(pk=pk)
#             serializer = TaskSerializer(task, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Task.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Event, Attendee, Task
from .serializers import EventSerializer, AttendeeSerializer, TaskSerializer
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

# def event_management(request):
#     if request.method == 'GET':
#         events = Event.objects.all()
#         return render(request, 'event_management.html', {'events': events})
#     elif request.method == 'POST':
#         serializer = EventSerializer(data=request.POST)
#         if serializer.is_valid():
#             serializer.save()
#             return redirect('event_management')  # Redirect to the event management page after saving
#         events = Event.objects.all()  # Fetch events again to show in case of error
#         return render(request, 'event_management.html', {'events': events, 'errors': serializer.errors})

# # Event Management API
# class EventViewSet(viewsets.ViewSet):
#     def create(self, request):
#         serializer = EventSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def list(self, request):
#         events = Event.objects.all()
#         serializer = EventSerializer(events, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         try:
#             event = Event.objects.get(pk=pk)
#             serializer = EventSerializer(event)
#             return Response(serializer.data)
#         except Event.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def update(self, request, pk=None):
#         try:
#             event = Event.objects.get(pk=pk)
#             serializer = EventSerializer(event, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Event.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def destroy(self, request, pk=None):
#         try:
#             event = Event.objects.get(pk=pk)
#             event.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Event.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

from django.shortcuts import render
from .models import Event
from .serializers import EventSerializer

def event_management(request):
    events = Event.objects.all()  # Fetch all events
    return render(request, 'event_management.html', {'events': events})
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            event = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        events = self.get_queryset()
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            event = self.get_queryset().get(pk=pk)
            serializer = self.get_serializer(event)
            return Response(serializer.data)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            event = self.get_queryset().get(pk=pk)
            serializer = self.get_serializer(event, data=request.data)
            if serializer.is_valid():
                event = serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            event = self.get_queryset().get(pk=pk)
            event.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)



# Similar views for Attendee and Task can be added here...
# def attendee_management(request):
#     if request.method == 'GET':
#         attendees = Attendee.objects.all()
#         return render(request, 'attendee_management.html', {'attendees': attendees})
#     elif request.method == 'POST':
#         serializer = AttendeeSerializer(data=request.POST)
#         if serializer.is_valid():
#             serializer.save()
#             return redirect('attendee_management')  # Redirect to the attendee management page after saving
#         attendees = Attendee.objects.all()  # Fetch attendees again to show in case of error
#         return render(request, 'attendee_management.html', {'attendees': attendees, 'errors': serializer.errors})

# # Attendee Management API
# class AttendeeViewSet(viewsets.ViewSet):
#     def create(self, request):
#         serializer = AttendeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def list(self, request):
#         attendees = Attendee.objects.all()
#         serializer = AttendeeSerializer(attendees, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         try:
#             attendee = Attendee.objects.get(pk=pk)
#             serializer = AttendeeSerializer(attendee)
#             return Response(serializer.data)
#         except Attendee.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def update(self, request, pk=None):
#         try:
#             attendee = Attendee.objects.get(pk=pk)
#             serializer = AttendeeSerializer(attendee, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Attendee.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def destroy(self, request, pk=None):
#         try:
#             attendee = Attendee.objects.get(pk=pk)
#             attendee.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Attendee.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Attendee
from .serializers import AttendeeSerializer

def attendee_management(request):
    if request.method == 'GET':
        attendees = Attendee.objects.all()
        return render(request, 'attendee_management.html', {'attendees': attendees})
    elif request.method == 'POST':
        serializer = AttendeeSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('attendee_management')  # Redirect to the attendee management page after saving
        attendees = Attendee.objects.all()  # Fetch attendees again to show in case of error
        return render(request, 'attendee_management.html', {'attendees': attendees, 'errors': serializer.errors})

# Attendee Management API
# class AttendeeViewSet(viewsets.ViewSet):
#     queryset = Attendee.objects.all()
#     serializer_class = AttendeeSerializer
    
#     def create(self, request):
#         serializer = AttendeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def partial_update(self, request, pk=None):
#         try:
#             attendee = self.get_object()
#             assigned_event_id = request.data.get('assigned_event')
#             if assigned_event_id:
#                 attendee.assigned_event_id = assigned_event_id
#                 attendee.save()
#             return Response(AttendeeSerializer(attendee).data, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
#     def list(self, request):
#         attendees = Attendee.objects.all()
#         serializer = AttendeeSerializer(attendees, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         try:
#             attendee = Attendee.objects.get(pk=pk)
#             serializer = AttendeeSerializer(attendee)
#             return Response(serializer.data)
#         except Attendee.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def update(self, request, pk=None):
#         try:
#             attendee = Attendee.objects.get(pk=pk)
#             serializer = AttendeeSerializer(attendee, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Attendee.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def destroy(self, request, pk=None):
#         try:
#             attendee = Attendee.objects.get(pk=pk)
#             attendee.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Attendee.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Attendee, Event
from .serializers import AttendeeSerializer, EventSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Attendee
from .serializers import AttendeeSerializer

class AttendeeViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            attendees = Attendee.objects.all()
            serializer = AttendeeSerializer(attendees, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        try:
            serializer = AttendeeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        try:
            attendee = Attendee.objects.get(pk=pk)
            serializer = AttendeeSerializer(attendee)
            return Response(serializer.data)
        except Attendee.DoesNotExist:
            return Response({'error': 'Attendee not found'}, status=status.HTTP_404_NOT_FOUND)

   
    def update(self, request, pk=None):
        try:
            attendee = Attendee.objects.get(pk=pk)
            serializer = AttendeeSerializer(attendee, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Attendee.DoesNotExist:
            return Response({'error': 'Attendee not found'}, status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        try:
            attendee = Attendee.objects.get(pk=pk)
            serializer = AttendeeSerializer(attendee, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Attendee.DoesNotExist:
            return Response({'error': 'Attendee not found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            attendee = Attendee.objects.get(pk=pk)
            attendee.delete()
            return Response({'message': 'Attendee deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Attendee.DoesNotExist:
            return Response({'error': 'Attendee not found'}, status=status.HTTP_404_NOT_FOUND)


# def task_tracker(request):
#     if request.method == 'GET':
#         tasks = Task.objects.all()
#         return render(request, 'task_tracker.html', {'tasks': tasks})
#     elif request.method == 'POST':
#         serializer = TaskSerializer(data=request.POST)
#         if serializer.is_valid():
#             serializer.save()
#             return redirect('task_tracker')  # Redirect to the task tracker page after saving
#         tasks = Task.objects.all()  # Fetch tasks again to show in case of error
#         return render(request, 'task_tracker.html', {'tasks': tasks, 'errors': serializer.errors})
# # Task Management API
# class TaskViewSet(viewsets.ViewSet):
#     def create(self, request):
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def list(self, request):
#         event_id = request.query_params.get('event_id', None)
#         if event_id is not None:
#             tasks = Task.objects.filter(event_id=event_id)
#         else:
#             tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         try:
#             task = Task.objects.get(pk=pk)
#             serializer = TaskSerializer(task)
#             return Response(serializer.data)
#         except Task.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def update(self, request, pk=None):
#         try:
#             task = Task.objects.get(pk=pk)
#             serializer = TaskSerializer(task, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Task.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def destroy(self, request, pk=None):
#         try:
#             task = Task.objects.get(pk=pk)
#             task.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Task.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)



from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Task, Event, Attendee
from .serializers import TaskSerializer, EventSerializer, AttendeeSerializer

def task_tracker(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        events = Event.objects.all()
        attendees = Attendee.objects.all()
        return render(request, 'task_tracker.html', {
            'tasks': tasks,
            'events': events,
            'attendees': attendees
        })
    elif request.method == 'POST':
        task_id = request.POST.get('task_id')
        if task_id:
            task = Task.objects.get(id=task_id)
            serializer = TaskSerializer(task, data=request.POST)
        else:
            serializer = TaskSerializer(data=request.POST)

        if serializer.is_valid():
            serializer.save()
            return redirect('task_tracker')  # Redirect to the task tracker page after saving
        tasks = Task.objects.all()  # Fetch tasks again to show in case of error
        events = Event.objects.all()
        attendees = Attendee.objects.all()
        return render(request, 'task_tracker.html', {
            'tasks': tasks,
            'events': events,
            'attendees': attendees,
            'errors': serializer.errors
        })
# class TaskViewSet(viewsets.ViewSet):
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request):
        """
        List all tasks. Filters by event if 'event_id' is provided.
        """
        event_id = request.query_params.get('event_id', None)
        if event_id:
            tasks = Task.objects.filter(event_id=event_id)
        else:
            tasks = Task.objects.all()
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Task.DoesNotExist:
            return Response({'detail': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # def list(self, request):
   
    #     event_id = request.query_params.get('event_id', None)
    #     if event_id:
    #         tasks = Task.objects.filter(event_id=event_id)
    #     else:
    #         tasks = Task.objects.all()  # Fetch all tasks if no event_id is provided
    #     serializer = TaskSerializer(tasks, many=True)
    #     return Response(serializer.data)

    # def list(self, request):
    #     event_id = request.query_params.get('event_id', None)
    #     if event_id is not None:
    #         tasks = Task.objects.filter(event_id=event_id)
    #     else:
    #         tasks = Task.objects.all()
    #     serializer = TaskSerializer(tasks, many=True)
    #     return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # def update(self, request, pk=None):
    #     try:
    #         task = Task.objects.get(pk=pk)
    #         serializer = TaskSerializer(task, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     except Task.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            task = Task.objects.get(pk=pk)
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)