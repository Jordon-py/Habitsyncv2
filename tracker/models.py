from django.db import models
from django.contrib.auth.models import User

FREQUENCY_CHOICES = [
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('yearly', 'Yearly'),
]

# Create your models here.
class Habit(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, default='daily')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return (f"Habit(name='{self.name}', description='{self.description}', "
                f"created_at='{self.created_at}', updated_at='{self.updated_at}', "
                f"completed={self.completed}, frequency='{self.frequency}', "
                f"start_date='{self.start_date}', end_date='{self.end_date}')")
