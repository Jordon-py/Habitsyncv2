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
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-default-dev-key-change-in-production')
if os.environ.get('DYNO') and SECRET_KEY == 'django-insecure-default-dev-key-change-in-production':
    raise RuntimeError("SECRET_KEY environment variable not set in production. Aborting...")

# Default: False for production (Heroku)
DEBUG = os.environ.get('DEBUG', 'False').lower() in ('true', '1', 't')
if os.environ.get('DYNO'):  # Running on Heroku
    DEBUG = False

# Parse ALLOWED_HOSTS from environment
ALLOWED_HOSTS = [host.strip() for host in os.environ.get(
    'ALLOWED_HOSTS',
    'localhost,127.0.0.1,habitsync-4c41c4781ea2.herokuapp.com'
).split(',')]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sessions',
    'tracker',
    'whitenoise.runserver_nostatic',  # Add this for better local static file serving with WhiteNoise
]

# Whitenoise check
USE_WHITENOISE = True  # Always use WhiteNoise on Heroku

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise should always be enabled for Heroku
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'habitsync.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'tracker', 'templates')],
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

WSGI_APPLICATION = 'habitsync.wsgi.application'

# Database
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get(
            'DATABASE_URL',
            'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
        ),
        conn_max_age=600,
    )
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files configuration - ensure this is properly set
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'tracker', 'static'),
]

# WhiteNoise for production
if USE_WHITENOISE:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
else:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Redirect URLs
LOGIN_REDIRECT_URL = 'tracker:home'
LOGOUT_REDIRECT_URL = 'tracker:home'
LOGIN_URL = 'tracker:login'
