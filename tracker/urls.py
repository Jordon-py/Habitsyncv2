from django.urls import path
from . import views

app_name = "tracker"

urlpatterns = [
    path('', views.home, name='home'),  # Home page for empty path
    path('habits/', views.habits, name='habits'),
    path('create/', views.create, name='create'),
    path('update/<int:habit_id>/', views.update, name='update'),
    path('delete/<int:habit_id>/', views.delete, name='delete'),
    path('habit/<int:habit_id>/', views.habit, name='habit'),
    path('habit/<int:habit_id>/record/', views.record, name='record'),
    path('habit/<int:habit_id>/delete/', views.delete_record, name='delete_record'),
    path('habit/<int:habit_id>/update/', views.update_record, name='update_record'),
    path('habit/<int:habit_id>/complete/', views.complete, name='complete'),
    path('habit/<int:habit_id>/incomplete/', views.incomplete, name='incomplete'),
    path('habit/<int:habit_id>/stats/', views.stats, name='stats'),
    path('about/', views.about, name='about'),  # Added about URL pattern
]
