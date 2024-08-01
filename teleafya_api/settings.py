from pathlib import Path
import environ
import os
import datetime
import django_heroku
import dj_database_url
from decouple import config

def check_env(environmental_variable):
    if environmental_variable in os.environ:
        return environmental_variable
    else:
        return ""
# Initialize environment variables
env = environ.Env(
    DEBUG=(bool, False)
)

# Set the project base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
environ.Env.read_env()

# Debug mode
DEBUG = env('DEBUG')

# Secret key
SECRET_KEY = env('SECRET_KEY')

# Allowed hosts
ALLOWED_HOSTS = ['djangorestteleafya-a20e658a1b93.herokuapp.com']

# Custom user model
AUTH_USER_MODEL = "authentication.User"

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'drf_yasg',
    'authentication',
    'django_filters',
    'appointments',
    'billing',
    'payment_status',
]

# Swagger settings
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL configuration
ROOT_URLCONF = 'teleafya_api.urls'

# Templates
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

# WSGI application
WSGI_APPLICATION = 'teleafya_api.wsgi.application'

# Database configuration
# DATABASES = {
#     'default': dj_database_url.config(default=config('DATABASE_URL'))
# }


# Retrieve the DATABASE_URL from environment variables
# DB_URL = env('DATABASE_URL')

DATABASES = {}

DB_URL = str(os.getenv('DATABASE_URL'))

if DB_URL != 'None':
    DATABASES = {'default': dj_database_url.config(env="DATABASE_URL", default=DB_URL, conn_max_age=600)}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'teleafya',
            'USER': 'postgres',
            'PASSWORD': env('PASSWORD'),
            'HOST': 'localhost',
            'PORT': '5432',
        },
    }
print(DB_URL)
print(DATABASES)


# DATABASES = {
#     'default': dj_database_url.config(
#         default=check_env("FIRST_DB") or check_env("THIRD_DB"),
#         conn_max_age=600
#     )
# }




# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'ddie988ljc9ptp',
#         'USER': 'u599b1vinddp3u',
#         'PASSWORD': 'pfd7b473af78a91ca88e513af39f01e720d2317dfdd057a1a56bd327de50f8858',
#         'HOST': 'ce0lkuo944ch99.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com',
#         'PORT': '5432',
#     }
# }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
# REST framework settings

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
    'NON_FIELD_ERRORS_KEY': 'error',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# Simple JWT settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=10),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
}

# Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# CORS settings
CORS_ALLOW_ALL_ORIGINS = True

# Static files
STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_SSL = False
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}

# Heroku settings
# django_heroku.settings(locals(), databases=False)
django_heroku.settings(locals())
