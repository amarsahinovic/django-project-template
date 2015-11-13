# -*- coding: UTF-8 -*-
import os
import sys

# One level more then the default generated BASE_DIR since we have settings in directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

root = lambda * x: os.path.normpath(os.path.join(os.path.abspath(BASE_DIR), *x))
sys.path.append(BASE_DIR)

ADMINS = (
   # ('Your name', 'yourname@example.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'Europe/Sarajevo'
LANGUAGE_CODE = 'bs-ba'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

DATE_FORMAT = '%d.%m.%Y.'
DATETIME_FORMAT = '%d.%m.%Y. %H:%i'

DATE_INPUT_FORMATS = (DATE_FORMAT,)
DATETIME_INPUT_FORMATS = (DATETIME_FORMAT,)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = (
    root('static'),
)

STATIC_ROOT = root('..', 'public', 'static')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

MEDIA_ROOT = root('..', 'public', 'media')
MEDIA_URL = '/media/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    root('templates'),
)

SECRET_KEY = r'{{ secret_key }}'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

ROOT_URLCONF = '{{ project_name }}.urls'
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

SESSION_ENGINE = 'redis_sessions.session'
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

THIRD_PARTY_APPS = (
    'foundation',
    'django_extensions',
    'djcelery',
    'compressor',
)

LOCAL_APPS = (
    'pages',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_HOST_USER = 'postmaster@--- CHANGE ME ---'
EMAIL_HOST_PASSWORD = '--- CHANGE ME ---'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)
