from django.apps import AppConfig


class ForumConfig(AppConfig):
    """
    Configuration for the forum app.

    Data is obtained from:
    - Django settings and configurations.

    Data is returned as:
    - A configured app ready to be used in the Django project.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forum'
