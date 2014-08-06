from .base import *
import os
import dj_database_url

try:
    from urlparse import urlparse
except ImportError as e:
    from urllib.parse import urlparse

print('Using development settings')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS += (
    'debug_toolbar',
)

INTERNAL_IPS = ('127.0.0.1')

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

DATABASE_USER = 'dbuser'
DATABASE_PASSWORD = 'dbpass'
DATABASE_NAME = 'dbname'
DATABASE_URL = 'postgres://{0}:{1}@localhost:5432/{2}'.format(DATABASE_USER,
                                                        DATABASE_PASSWORD,
                                                        DATABASE_NAME)

DATABASE_URL = os.getenv('DATABASE_URL', DATABASE_URL)
DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}

REDIS_URL = 'redis://localhost:6379'
REDIS_URL = os.getenv('REDIS_URL', REDIS_URL)
REDIS = urlparse(REDIS_URL)

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '%s:%s:1' % (REDIS.hostname, REDIS.port),
        'OPTIONS': {
            'PASSWORD': REDIS.password,
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            "CLIENT_CLASS": "redis_cache.client.HerdClient",
        }
    }
}

BROKER_URL = REDIS_URL
BROKER_TRANSPORT_OPTIONS = {'fanout_prefix': True}
CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
CELERY_ACCEPT_CONTENT = ['pickle', 'json']

SESSION_REDIS_PREFIX = 'session'

