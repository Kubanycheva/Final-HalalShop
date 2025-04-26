from django.apps import AppConfig


class HalalAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'halal_app'

    def ready(self):
        import halal_app.signals
