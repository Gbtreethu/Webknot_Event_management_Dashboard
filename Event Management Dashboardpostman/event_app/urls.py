# # urls.py
# from django.urls import path
# from rest_framework.routers import DefaultRouter
# from .views import EventViewSet, AttendeeViewSet, TaskViewSet

# router = DefaultRouter()
# router.register(r'events', EventViewSet, basename='event')
# router.register(r'attendees', AttendeeViewSet, basename='attendee')
# router.register(r'tasks', TaskViewSet, basename='task')

# urlpatterns = router.urls
# urls.py

# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, AttendeeViewSet, TaskViewSet, event_management, index

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')
router.register(r'attendees', AttendeeViewSet, basename='attendee')
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('api/', include(router.urls)),
   
    
]