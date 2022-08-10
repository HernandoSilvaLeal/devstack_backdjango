
from pathlib import Path
from datetime import timedelta
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bs+3)=132_&x9enyxo@08r*kqly$&z(l*ayw_b4myk4^m_69iw'

DEBUG = True

ALLOWED_HOSTS = []

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# Application definition

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
<<<<<<< HEAD
    'apps.activities',
    'apps.assets',
    'apps.base',
    'apps.metrics',
    'apps.standards',
    'apps.resources',
    'apps.projects',
    'apps.users',
=======
    'apps.base'
    'apps.users'
    'apps.projects'
    'apps.assets'
    'apps.activities'
    'apps.metrics'
    'apps.resources'
    'apps.standards'
>>>>>>> f6e5928acd2d26fadb59eb29eef986d6ade355c4
]


THIRD_APPS = [
<<<<<<< HEAD
    'corsheaders',
    # 'automatic_crud',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',  
    'rest_framework_simplejwt.token_blacklist',  
    'simple_history',
    'drf_yasg',
=======
    # 'corsheaders',
    # 'automatic_crud',
    # 'rest_framework',
    # 'rest_framework.authtoken',
    # 'rest_framework_simplejwt',  
    # 'rest_framework_simplejwt.token_blacklist',  
    'simple_history',
    # 'drf_yasg',
>>>>>>> f6e5928acd2d26fadb59eb29eef986d6ade355c4
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

<<<<<<< HEAD
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}
# IMPORTANTE LEER para dejer algunos enpoints publicos = https://es.stackoverflow.com/questions/415622/como-hacer-para-que-un-endpoint-no-me-exija-el-token-en-django
=======

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ],
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     )
# }

>>>>>>> f6e5928acd2d26fadb59eb29eef986d6ade355c4

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
<<<<<<< HEAD
    'corsheaders.middleware.CorsMiddleware',
=======
    #'corsheaders.middleware.CorsMiddleware',
>>>>>>> f6e5928acd2d26fadb59eb29eef986d6ade355c4
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
<<<<<<< HEAD
]

=======


]

SWAGGER_SETTINGS = {
    'DOC_EXPANSION': 'none'
}

>>>>>>> f6e5928acd2d26fadb59eb29eef986d6ade355c4
ROOT_URLCONF = 'devstackcore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': [BASE_DIR / 'templates'], Añado el directorio de templates donde debe buscar QUE renderizar los url patters del archivo urls.py de las apps
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Import os + variable BASE_DIR
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

WSGI_APPLICATION = 'devstackcore.wsgi.application'
<<<<<<< HEAD
=======


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


>>>>>>> f6e5928acd2d26fadb59eb29eef986d6ade355c4

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


<<<<<<< HEAD
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User' 
# Error de conflicto solucionado = https://stackoverflow.com/questions/43871604/valueerror-dependency-on-app-with-no-migrations-customuser 
=======
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'
>>>>>>> f6e5928acd2d26fadb59eb29eef986d6ade355c4

CORS_ORIGIN_WHITELIST = [
    "http://localhost:8000",
    "http://localhost:3000"
]

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
<<<<<<< HEAD
    'BLACKLIST_AFTER_ROTATION': False
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'



SWAGGER_SETTINGS = {
    'DOC_EXPANSION':'none',
}

REDOC_SETTINGS = {
}













=======
    'BLACKLIST_AFTER_ROTATION': True
}

>>>>>>> f6e5928acd2d26fadb59eb29eef986d6ade355c4




"""
<<<<<<< HEAD
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

# Error RuntimeError: Conflicting 'historicalareasmodel' models in application 'projects': <class 'apps.projects.api.models.HistoricalAreasModel'> and <class 'apps.projects.admin.HistoricalAreasModel'>.
# https://stackoverflow.com/questions/39574665/django-oscar-runtimeerror-conflicting-models
# El error era que las clases tenian el mismo nombre y generaban un error en tiempo de ejecucion ---> <class AreasAdmin(models.AreasModel):> -----> <class AreasModel(CompaniesModel):>

# Error en una relacion circular entre el atriburto de la clase y el atributo del campo, la solucion fue cambiar la base del modelo, lo resolvi analizando la construccion del modelo y leyendo el error varias vecces en español
# En models de projects---> class AreasModel(CompaniesModel): --->  company = models.ForeignKey(CompaniesModel, verbose_name="Empresa", on_delete=models.CASCADE) ---> solucion 

# System check identified 16 issues (0 silenced).
# ←[31;1mactivities.ControlsAdmin: (models.E020) The 'ControlsAdmin.check()' class method is currently overridden by <django.db.models.query_utils.DeferredAttribute object at 0x0000018B11632110>.←[0m

# AttributeError: module 'django.contrib.admin' has no attribute 'AssetsModel'
# El error es que estaba llamando al modelo erradamente como class AssetsAdmin(admin.AssetsModel): cuando lo correcto es ---> 

# ←[31;1massets.InformationassetsAdmin: (models.E020) The 'InformationassetsAdmin.check()' class method is currently overridden by <django.db.models.query_utils.DeferredAttribute object at 0x0000024398774BB0>.←[0m 
# La solucion al error es no usar palabras reservadas porque el intgerprete de django cofunde las definiciones por eso indica que las funciones se sobreescriben.

# ←[31;1massets.InformationassetsModel.category_assets: (fields.E305) Reverse query name for 'assets.InformationassetsModel.category_assets' clashes with reverse query name for 'assets.InformationassetsModel.assetsmodel_ptr'.
# HINT: Add or change a related_name argument to the definition for 'assets.InformationassetsModel.category_assets' or 'assets.InformationassetsModel.assetsmodel_ptr'.←[0m
# El error significa que hay una relacion circular, se basa en un modelo que tambien se llama como foraneo, la solucion es quitar el campo o cambiar la base de modelo en el atributo de la clase

# AttributeError: module 'django.contrib.admin' has no attribute 'ProgressreportModel' en e "C:\_devprog\Project\devstack_backdjango_python\apps\metrics\admin.py", line 12, in <module> class ProgressreportAdmin(admin.ProgressreportModel):
# El error es que la importacion esta mal referenciada, se esta utilizando la palabra admin y no model

# AssertionError: 'Logout' should either include a `serializer_class` attribute, or override the `get_serializer_class()` method.
# Este error se genera porque en el logout no se ubico ningun serializador
# Se soluciono, ubicando el serializer_class en la clase logut del views de users ----> serializer_class = CustomTokenObtainPairSerializer
# https://stackoverflow.com/questions/62099191/genericapiview-should-either-include-a-serializer-class-attribute-or-override 
# https://github.com/axnsan12/drf-yasg/issues/694

# Error al correr las migraciones, no las completaba porque en la app metrics habia un modelo con campos foraneos que hacien relacion aun campo y eso no es permitido, solo se puyede relacionar el modelo pero no un campo en especifico
# ←[31m  Your models in app(s): 'metrics' have changes that are not yet reflected in a migration, and so won't be applied.←[0m
# ←[31m  Run 'manage.py makemigrations' to make new migrations, and then re-run 'manage.py migrate' to apply them.←[0m
# Lo solucione haciendo referencia foranea solo al modelo y borrando la referencia al campo, luego ejecute makemigrations y luego migrste y corrio nomral

# Para que u endpoint no exija autenticacion django ---> permission_classes = [permissions.AllowAny] dentro de la clase
# https://es.stackoverflow.com/questions/415622/como-hacer-para-que-un-endpoint-no-me-exija-el-token-en-django

# Queria cambiar el fondo de color de django admin, encontre como, cree el enturamientos y los paths y la carpeta templates quedo al pelo :D 
# https://stackoverflow.com/questions/1926049/django-templatedoesnotexist#:~:text=Django%20TemplateDoesNotExist%20error%20means%20simply,.py%20)%20by%20TEMPLATE_DIRS%20setting.











# ============> AUN SIN SOLUCIONAR hay algunos campos de los modelos que se pueden migrar, presumo que son los choises, o algunos default
# ValueError: Cannot serialize: <django.db.models.query_utils.DeferredAttribute object at 0x00000207C5DBB370>
# There are some values Django cannot serialize into migration files.
# For more, see https://docs.djangoproject.com/en/4.0/topics/migrations/#migration-serializing
=======
Django settings for devstackcore project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

>>>>>>> f6e5928acd2d26fadb59eb29eef986d6ade355c4
