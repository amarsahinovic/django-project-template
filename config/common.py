# Common settings for all enviroments

import os
import sys

# Get project root and append it
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)
# Append apps and libs so we can import from them directly
sys.path.append(os.path.join(PROJECT_ROOT , 'apps'))
sys.path.append(os.path.join(PROJECT_ROOT , 'libs'))


DEBUG = True
TEMPLATE_DEBUG = DEBUG


ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)


MANAGERS = ADMINS
TIME_ZONE = 'Europe/Sarajevo'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True


# User uploaded media dir, set to media directory in project root
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media').replace('\\','/')
MEDIA_URL = '/media/'


# Set static url and static directory to apps/static
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'apps', 'static').replace('\\','/'),
)


# Where to look for out static files
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)


# This is where collectstatic will collect all the files,
# Make this top-level static dir, not the apps/static
# DO NOT put files in this directory by yourself, use collectstatic
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static').replace('\\','/')


# Override this in local/production settings
SECRET_KEY = 'qwertzuiop1234567890ASDFGHJKL'


# Where to load our templates from
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    
)


# Template dir, set to apps/templates
# Per app templates should be in apps/templates/APPNAME/
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'apps', 'templates').replace('\\','/')
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)


# Middleware 
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)


ROOT_URLCONF = 'urls'


INSTALLED_APPS = (
    #django.contrib.auth',
    #'django.contrib.contenttypes',
    #'django.contrib.sessions',
    #'django.contrib.sites',
    #'django.contrib.messages',
    #'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    #'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    
    'apps.app1',
    'apps.core',
    
    # Migration app
    #'south',
)