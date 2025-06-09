from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        from django.contrib.auth import get_user_model
        from django.db.utils import OperationalError, ProgrammingError

        User = get_user_model()
        try:
            if not User.objects.exists():
                User.objects.create_superuser('admin', 'admin@example.com', 'myco')
        except (OperationalError, ProgrammingError):
            # Database might not be ready yet
            pass
