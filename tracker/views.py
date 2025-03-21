from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Habit
from .forms import HabitForm
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

# Home view renders the dashboard using home.html
def home(request):
    if request.user.is_authenticated:
        # Retrieve habits for the logged-in user
        habits = Habit.objects.filter(user=request.user)
        return render(request, 'dashboard.html', {'habits': habits})
    else:
        habits = []
    return render(request, 'home.html', {'habits': habits})

def about(request):
    return render(request, 'about.html', {})

@login_required
def habits(request):
    habits = Habit.objects.filter(user=request.user)
    return render(request, 'habits.html', {'habits': habits})

@login_required
def create(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            # Create habit but don't save to DB yet
            habit = form.save(commit=False)
            # Add current user to habit
            habit.user = request.user
            # Save to DB
            habit.save()
            return redirect('tracker:habits')
    else:
        form = HabitForm()
    
    return render(request, 'create.html', {'form': form})


@login_required
def update(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect('tracker:habits')
    else:
        form = HabitForm(instance=habit)
    
    return render(request, 'update.html', {'form': form, 'habit': habit})

@login_required
def delete(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    
    if request.method == 'POST':
        habit.delete()
        return redirect('tracker:habits')
    
    return render(request, 'delete.html', {'habit': habit})

@login_required
def habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    return render(request, 'habit_detail.html', {'habit': habit})

@login_required
def record(request, habit_id):
    # For future implementation
    return HttpResponse(f"Record Habit {habit_id}")

@login_required
def delete_record(request, habit_id):
    # For future implementation
    return HttpResponse(f"Delete Record for Habit {habit_id}")

@login_required
def update_record(request, habit_id):
    # For future implementation
    return HttpResponse(f"Update Record for Habit {habit_id}")

@login_required
def complete(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    habit.completed = True
    habit.save()
    return redirect('tracker:habit', habit_id=habit_id)

@login_required
def incomplete(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    habit.completed = False
    habit.save()
    return redirect('tracker:habit', habit_id=habit_id)

@login_required
def stats(request, habit_id):
    # For future implementation
    return HttpResponse(f"Stats for Habit {habit_id}")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tracker:home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
