"""
URL configuration for habitsync project.
"""

from django.contrib import admin
from django.urls import path, include

# Override admin permission check to allow any authenticated user (for testing only)
admin.site.has_permission = lambda request: request.user.is_authenticated

urlpatterns = [
    path('admin/', admin.site.urls),
    # Remove the duplicate inclusion and just include the tracker.urls once
    path('', include('tracker.urls')),
]
