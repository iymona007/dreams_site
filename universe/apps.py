from django.apps import AppConfig


class UniverseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'universe'
    verbose_name = 'DREAMS Universe'

    def ready(self):
        from . import signals  # noqa: F401
