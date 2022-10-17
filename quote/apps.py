from django.apps import AppConfig


class QuoteAppConfig(AppConfig):
    name = 'quote'

    def ready(self):
        import quote.signals
