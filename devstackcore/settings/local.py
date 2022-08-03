import os
from .base import *

DEBUG = True

ALLOWED_HOSTS = []

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

STATIC_URL = '/static/'

STATICFILES_DIRS = (BASE_DIR, 'static')

MEDIA_URL = '../media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')