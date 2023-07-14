"""
Django settings for lakshya project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-mx8k&bjf)g6iszm2&ua77b&(s+wam90+5*o=pgc^c6a3#t9gdr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# This is to configure the settnigs for serving static files 
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '')

# Reading Configuration File
config = {}
try:
    with open('./config.conf') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):  # Ignore empty lines and comments
                key, value = line.split('=', 1)
                config[key.strip()] = value.strip()
except:
    pass

ALLOWED_HOSTS = [
    # Removing http:// and https:// from host names
    config['NGROK'].split("//")[1],  
    config['REACT_WEB'].split("//")[1],
]

CORS_ALLOWED_ORIGINS = [
    config['NGROK'],
    config['REACT_WEB'],
]
CORS_ORIGIN_ALLOW_ALL = False


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'corsheaders',
    "django_extensions",
    #User apps
    
    'material.apps.MaterialConfig',
    'jobs.apps.JobsConfig',
    'events.apps.EventsConfig',
    'education.apps.EducationConfig',
    'common.apps.CommonConfig',
    'authentication.apps.AuthenticationConfig',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lakshya.urls'

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

WSGI_APPLICATION = 'lakshya.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# CROSS ORIGIN REQUEST SETTINGS

CORS_ORIGIN_WHITELIST = [ 
    config['NGROK'],
    config['REACT_WEB'],
]

CORS_ALLOW_HEADERS = [
    'Accept',
    'Accept-Encoding',
    'Authorization',
    'Content-Type',
    'Cookie',  # Add 'Cookie' header to allow
    'Origin',
]

CORS_ALLOWED_METHODS = [
    'GET',
    'POST',
    'OPTIONS',
    # Add other allowed methods as needed
]


CORS_ALLOW_CREDENTIALS = True


# SESSION_COOKIE_HTTPONLY = True
# SESSION_COOKIE_SECURE = True
# SESSION_COOKIE_SAMESITE = "None"
# SESSION_COOKIE_PATH = '/'
# SESSION_COOKIE_DOMAIN = "None"



# CSRF_TRUSTED_ORIGINS = [
#     config['NGROK'],
#     config['REACT_WEB'], 
# ]

# CSRF_COOKIE_HTTPONLY = False
# CSRF_COOKIE_SAMESITE = None
# CSRF_COOKIE_DOMAIN = None


