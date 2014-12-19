from django.apps import AppConfig


class AlacarteConfig(AppConfig):
    """The default AppConfig for alacarte which does autodiscovery."""

    name = 'alacarte'

    def ready(self):
        self.module.autodiscover()
