from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'                                     # Es importante usar aqui el nombre con la sub ruta si no arroja error
                                                            # https://stackoverflow.com/questions/67056517/django-3-2-exception-django-core-exceptions-improperlyconfigured
