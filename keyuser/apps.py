from django.apps import AppConfig


class KeyuserAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'keyuser'

    def ready(self):
        import keyuser.signals
