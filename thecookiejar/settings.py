"""
Django settings for thecookiejar project.
Generated by 'django-admin startproject' using Django 4.0.3.
For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import socket
import psycopg2 
import dj_database_url
import cloudinary_storage 
# from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader
import cloudinary.api

# load_dotenv()

# comment this out to work locally
# DATABASE_URL = os.environ.get('DATABASE_URL')
# conn = psycopg2.connect(DATABASE_URL, sslmode='require')

# THIS WHOLE THING COMMENTED OUT TO WORK LOCALLY
# If the host name starts with 'live', DJANGO_HOST = "production"
if socket.gethostname().startswith('live'):
    DJANGO_HOST = "production"
# Else if host name starts with 'test', set DJANGO_HOST = "test"
elif socket.gethostname().startswith('test'): 
    DJANGO_HOST = "testing"
else:
# If host doesn't match, assume it's a development server, set DJANGO_HOST = "development"
    DJANGO_HOST = "development"
# Define general behavior variables for DJANGO_HOST and all others
if DJANGO_HOST == "production":
    DEBUG = False
    STATIC_URL = 'https://thesweetcookiejar.herokuapp.com/'
else:
    DEBUG = True
    STATIC_URL = '/static/'



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = str(os.getenv('SECRET_KEY'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/



# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True  #comment this out when deploying!!!!!!! important!!!!!!!!!!!!!

# commented out to work locally uncomment when ready to deploy
ALLOWED_HOSTS = [
    # 'thesweetcookiejar.herokuapp.com' 
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main_app',
    # 'bootstrap5',
    'django_bootstrap5',
    'crispy_forms',
    'crispy_bootstrap5',
    'cloudinary',
    'cloudinary_storage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'thecookiejar.urls'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            '/www/STORE/main_app/templates/'
        ],
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

WSGI_APPLICATION = 'thecookiejar.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'thecookiejar',
    }
}



#commented out to work locally uncomment when ready to deploy
# DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True) 

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_URL = '/static/' comment out for deployment


# commented out to work locally uncomment when ready to deploy
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__)) 
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static') 



MEDIA_URL = '/media/'
# image uploading not working yet
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dq2v2nhpp',
    'API_KEY': str(os.getenv('API_KEY')),
    'API_SECRET': str(os.getenv('API_SECRET')),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# cloudinary.config( 
#     cloud_name = "dq2v2nhpp'", 
#     api_key = "734617347194513", 
#     api_secret = "9H2vE6MVfUzLzyevNHsuYoQSp2s",
# )
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = '/'