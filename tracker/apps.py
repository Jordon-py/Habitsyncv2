from django.apps import AppConfig


class TrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tracker'

class habitsyncConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'habitsync'  
