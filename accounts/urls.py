from django.urls import path
from .views import sign_in

urlpatterns = [
    path('login/', sign_in, name='login'),
]
