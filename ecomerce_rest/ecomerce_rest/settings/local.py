from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# ------> pip install psycopg2-binary para conexion a base de datos postgresql
DATABASES = { # pip install psycopg2-binary
    'default':{
        'ENGINE':'django.db.backends.postgresql',
        'HOST':'localhost',
        'PORT':'5432',
        'USER':'postgres',
        'PASSWORD':'Nandop*963',
        'NAME':'devstackdb',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
