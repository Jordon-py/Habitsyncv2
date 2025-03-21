"""
Django settings for habitsync project.
"""

import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# Try to load environment variables if python-dotenv is installed
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECR 'django-insecure-default-dev-key-change-in-production')

# Default: False for production (Heroku)
DEBUG = os.environ.get( 'False').lower() in  't')

# Parse ALLOWED_HOSTS from environment
ALLOWED_HOSTS = [host.strip() for host in os.environ.get(
    'ALLOWED
    'localhost,127.0.0.1,habitsync-4c41c4781ea2.herokuapp.com'
).')]

INSTALLED_APPS = [
    'django.contrib
    'django.contri
    'django.contrib.conten
    'django.contrib.me
    'django.contrib.stati
    'django.contrib.se
    't
    'whitenoise.runserver_no  # Add this for better local static file serving with WhiteNoise
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMidd
    'whitenoise.middleware.WhiteNoiseMidd  # WhiteNoise should be right after SecurityMiddleware
    'django.contrib.sessions.middleware.SessionMidd
    'django.middleware.common.CommonMidd
    'django.middleware.csrf.CsrfViewMidd
    'django.contrib.auth.middleware.AuthenticationMidd
    'django.contrib.messages.middleware.MessageMidd
    'django.middleware.clickjacking.XFrameOptionsMidd
]

ROOT_URLCONF = 'habitsync.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTem
        'DIRS': [os.path.join(BASE_DIR, 't 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors
                'django.template.context_processors.r
                'django.contrib.auth.context_processor
                'django.contrib.messages.context_processors.me
            ],
        },
    },
]

WSGI_APPLICATION = 'habitsync.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': ENGINE,
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityVal
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthVal
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordVal
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordVal
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 't 'static'),
]

# WhiteNoise for production static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Redirect URLs
LOGIN_REDIRECT_URL = 'tracker:home'
LOGOUT_REDIRECT_URL = 'tracker:home'
LOGIN_URL = 'tracker:login'

# HTTPS settings for production
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
