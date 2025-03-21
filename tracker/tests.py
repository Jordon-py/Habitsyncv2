from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Habit

class HabitTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )
        
        # Create a test habit
        self.habit = Habit.objects.create(
            name='Test Habit',
            description='This is a test habit',
            frequency='daily',
            user=self.user
        )
        
        # Set up the client
        self.client = Client()
    
    def test_home_view_logged_out(self):
        """Test the home view when user is logged out"""
        response = self.client.get(reverse('tracker:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
    
    def test_home_view_logged_in(self):
        """Test the home view when user is logged in"""
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('tracker:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')
    
    def test_habits_view_requires_login(self):
        """Test that the habits view requires login"""
        response = self.client.get(reverse('tracker:habits'))
        # Should redirect to login page
        self.assertEqual(response.status_code, 302)
    
    def test_habits_view_logged_in(self):
        """Test the habits view when user is logged in"""
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('tracker:habits'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'habits.html')
    
    def test_habit_detail_view(self):
        """Test the habit detail view"""
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('tracker:habit', args=[self.habit.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'habit_detail.html')
    
    def test_create_habit(self):
        """Test creating a new habit"""
        self.client.login(username='testuser', password='testpassword123')
        habit_data = {
            'name': 'New Habit',
            'description': 'A new habit for testing',
            'frequency': 'weekly'
        }
        response = self.client.post(reverse('tracker:create'), habit_data)
        # Should redirect to habits page after creation
        self.assertEqual(response.status_code, 302)
        # Check if the habit was created
        self.assertTrue(Habit.objects.filter(name='New Habit').exists())
    
    def test_complete_habit(self):
        """Test marking a habit as complete"""
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('tracker:complete', args=[self.habit.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect
        
        # Refresh habit from DB and check if it's marked as complete
        updated_habit = Habit.objects.get(id=self.habit.id)
        self.assertTrue(updated_habit.completed)
    
    def test_incomplete_habit(self):
        """Test marking a habit as incomplete"""
        # First mark the habit as complete
        self.habit.completed = True
        self.habit.save()
        
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('tracker:incomplete', args=[self.habit.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect
        
        # Refresh habit from DB and check if it's marked as incomplete
        updated_habit = Habit.objects.get(id=self.habit.id)
        self.assertFalse(updated_habit.completed)
