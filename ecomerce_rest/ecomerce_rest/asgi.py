"""
ASGI config for ecomerce_rest project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecomerce_rest.settings.local') # Actualizo la nueva ruta del archivo de configuracion settings (Se escribe el archivo sin la extension .py)

application = get_asgi_application()
