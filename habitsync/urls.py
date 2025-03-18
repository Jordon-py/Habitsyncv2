"""
URL configuration for habitsync project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
if not os.environ.get("DJANGO_SETTINGS_MODULE"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "habitsync.settings")

from django.contrib import admin
from django.urls import path, include

# Override admin permission check to allow any authenticated user (for testing only)
admin.site.has_permission = lambda request: request.user.is_authenticated

urlpatterns = [
    path('admin/', admin.site.urls),
    path('habit/', include('tracker.urls')),
    path('', include('tracker.urls')),
]
