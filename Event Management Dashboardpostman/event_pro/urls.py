# # event_pro/urls.py
# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from event_app.views import EventViewSet, AttendeeViewSet, TaskViewSet, event_management, index  # Replace 'your_app_name' with the actual app name

# router = DefaultRouter()
# router.register(r'events', EventViewSet, basename='event')
# router.register(r'attendees', AttendeeViewSet, basename='attendee')
# router.register(r'tasks', TaskViewSet, basename='task')
# from django.urls import path
# from event_app.views import index, event_management, attendee_management, EventViewSet, AttendeeViewSet, TaskViewSet

# urlpatterns = [
#     path('', index, name='landing_page'),  # This line defines the root URL
#     path('events/', event_management, name='event_management'),  # This should render the HTML
#     path('attendees/', attendee_management, name='attendee_management'),  # This line defines the attendee management URL
#     path('api/events/', EventViewSet.as_view({'get': 'list', 'post': 'create'}), name='event_api'),  # This is the API endpoint
#     path('api/attendees/', AttendeeViewSet.as_view({'get': 'list', 'post': 'create'}), name='attendee_api'),  # API for attendees
#     path('api/tasks/', TaskViewSet.as_view({'get': 'list', 'post': 'create'}), name='task_api'),  # API for tasks
# path('api/', include(router.urls)),
# ]
# # urlpatterns = [
# # #     path('', index, name='index'),
# # #     path('events/', EventViewSet.as_view({'get': 'list', 'post': 'create'}), name='event_management'),
# # #     # path('events/<int:pk>/', EventViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
# # #     path('attendees/', AttendeeViewSet.as_view({'get': 'list', 'post': 'create'}), name='attendee_management'),
# # #     path('attendees/<int:pk>/', AttendeeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
# # #     path('tasks/', TaskViewSet.as_view({'get': 'list', 'post': 'create'}), name='task_tracker'),
# # #     path('tasks/<int:pk>/', TaskViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
# # # path('events/', event_management, name='event_management'),  # Updated to use the new view
# # #     path('events/api/', EventViewSet.as_view({'get': 'list', 'post': 'create'}), name='event_api'),
# #    path('', index, name='landing_page'),  # This line defines the root URL
# #     path('events/', event_management, name='event_management'),  # This should render the HTML
# #     path('api/events/', EventViewSet.as_view({'get': 'list', 'post': 'create'}), name='event_api'),  # This is the API endpoint
# #     # path('attendees/', attendee_management, name='attendee_management'),  # Add this line for attendee management
# #     path('api/attendees/', AttendeeViewSet.as_view({'get': 'list', 'post': 'create'}), name='attendee_api'),  # API for attendees
# #     path('api/tasks/', TaskViewSet.as_view({'get': 'list', 'post': 'create'}), name='task_api'),  # API for tasks

# #     path('admin/', admin.site.urls),
# #     path('api/', include(router.urls)),  # Ensure this line is present
# # ]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from event_app.views import index, event_management, attendee_management, task_tracker, EventViewSet, AttendeeViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')
router.register(r'attendees', AttendeeViewSet, basename='attendee')
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', index, name='landing_page'),
    path('events/manage/', event_management, name='event_management'),  # Event management page
    path('attendees/manage/', attendee_management, name='attendee_management'),  # Attendee management page
    path('tasks/manage/', task_tracker, name='task_tracker'),  # Task tracker page
    path('api/', include(router.urls)),  # Include all API routes
]