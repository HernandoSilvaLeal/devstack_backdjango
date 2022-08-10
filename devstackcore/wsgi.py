"""
WSGI config for devstackcore project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devstackcore.settings.local')  

application = get_wsgi_application()


# DJANGO_SETTINGS_MODULE es la variable de entorno que almacenará todas las configuraciones de devstackcore.settings.local
# wsgi es como un bracito con el que manage.py ejecuta todo el progrma, yendo al __init__.py propio de django.conf.__init__.py
# asgi es como un bracito con el que manage.py ejecuta todo el progrma, yendo al __init__.py propio de django.conf.__init__.py
