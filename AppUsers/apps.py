from django.apps import AppConfig

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name= 'AppUsers'
    
    def ready(self):
        import AppUsers.signals  # noqa
