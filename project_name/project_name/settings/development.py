from .base import *
import os
import urlparse
import dj_database_url

print 'Using development settings'

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
REDIS = urlparse.urlparse(REDIS_URL)

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '%s:%s' % (REDIS.hostname, REDIS.port),
        'OPTIONS': {
            'DB': 0,
            'PASSWORD': REDIS.password,
            'PARSER_CLASS': 'redis.connection.HiredisParser'
        }
    }
}
