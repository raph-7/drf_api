from django.apps import AppConfig


class pos_guiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pos_gui'

    def ready(self):
        import pos_gui.signals