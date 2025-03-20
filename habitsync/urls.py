"""
URL configuration for habitsync project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the tracker URLs at the root path
    path('', include('tracker.urls')),
]
