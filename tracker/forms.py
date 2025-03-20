from django import forms
from .models import Habit

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'description', 'frequency']
        labels = {
            'name': 'Habit Name',
            'description': 'Habit Description',
            'frequency': 'Habit Frequency',
        }
        help_texts = {
            'name': 'Enter a descriptive name for your habit.',
            'description': 'Optionally, provide additional details about your habit.',
            'frequency': 'Select how often you want to track this habit.',
        }
        error_messages = {
            'name': {
                'max_length': "The habit name is too long.",
            },
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'frequency': forms.Select(attrs={'class': 'form-control'}),
        }
