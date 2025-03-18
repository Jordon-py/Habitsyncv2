from django.shortcuts import render
from django.http import HttpResponse
from .models import Habit
from django.contrib.auth.models import User

# Create your views here.
def habits(request):
    return HttpResponse("Habits")

def create(request):
    return HttpResponse("Create Habit")

def update(request, habit_id):
    return HttpResponse(f"Update Habit {habit_id}")

def delete(request, habit_id):
    return HttpResponse(f"Delete Habit {habit_id}")

def habit(request, habit_id):
    return HttpResponse(f"Habit {habit_id}")

def record(request, habit_id):
    return HttpResponse(f"Record Habit {habit_id}")

def delete_record(request, habit_id):
    return HttpResponse(f"Delete Record for Habit {habit_id}")

def update_record(request, habit_id):
    return HttpResponse(f"Update Record for Habit {habit_id}")

def complete(request, habit_id):
    return HttpResponse(f"Complete Habit {habit_id}")

def incomplete(request, habit_id):
    return HttpResponse(f"Incomplete Habit {habit_id}")

def stats(request, habit_id):
    return HttpResponse(f"Stats for Habit {habit_id}")