import os
from devstackcore.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/fref/settings/#databases
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
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = 'static/'
STATICFILES_DIRS = (BASE_DIR, 'static')
MEDIA_URL = '../media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')