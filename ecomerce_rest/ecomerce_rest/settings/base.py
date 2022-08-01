from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$id723b-_8$!n42&0=7feu8ltp$ix4(xu^ubcov**zve%^6juk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

BASE_APPS = [                           # Division de apps nativas de django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [                          # Division de de apps en desarrollo
    'apps.users',                       # Se creo esta nueva app para crear usuarios personalziados.
]

THIRD_APPS = [                          # Division de apps de terceros, ej Swagger.
    'rest_framework',   
    'simple_history',                   # Se agrega la nueva app de terceros, nos dira que usuario hizo que cambio en la base de datos.

    # 'rest_framework.authtoken',
    # 'drf_yasg',
    # 'corsheaders',                      # Añadimos la app ya que se acaba de instalar
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware', # Se agrega el middleware de la app instalada.
]

ROOT_URLCONF = 'ecomerce_rest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecomerce_rest.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', # Si hay espacios, se generar el error KEY: 'NAME'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = 'users.User'                      # Se apunta al modelo customizado para crear usuarios, se añadio la app y el middleware, Estructura = (app.class) 
                                                    # Si no se escribe bien da error porque no encuentra la clase dentro de la app
                                                    # django.core.exceptions.ImproperlyConfigured: AUTH_USER_MODEL refers to model 'users.Users' that has not been installed         

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
