from django.db import models
from django.contrib.auth.models import User


# Create your models here.
FREQUENCY_CHOICES = (
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('yearly', 'Yearly'),
)

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=80)
    description = models.TextField(blank=True)
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, default='daily')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    
    def __str__(self):
        return f"Habit: {self.name}, Description: {self.description}, User: {self.user.username}"
