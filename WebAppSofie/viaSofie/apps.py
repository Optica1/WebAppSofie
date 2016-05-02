from __future__ import unicode_literals

from django.apps import AppConfig


class ViasofieConfig(AppConfig):
    name = 'viaSofie'

    def ready(self): #for receiver & sending functions
        import viaSofie.signals