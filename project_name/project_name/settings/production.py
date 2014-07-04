from .base import *
import os
import urlparse
import dj_database_url

print 'Using production settings'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS += (
    'gunicorn',
    'raven.contrib.django.raven_compat',    
)

RAVEN_CONFIG = {
    'dsn': 'https://13c9305033704c7f8c50406dd7dd196d:9c15ce66590e4167b81db7bd05ce7e89@app.getsentry.com/18619',
}

DATABASE_USER = 'dbuser'
DATABASE_PASSWORD = 'dbpass'
DATABASE_NAME = 'dbname'
DATABASE_URL = 'postgres://{0}:{1}@localhost:5432/{2}'.format(DATABASE_USER,
                                                        DATABASE_PASSWORD,
                                                        DATABASE_NAME)

DATABASE_URL = os.getenv('DATABASE_URL', DATABASE_URL)
DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}
DATABASES['default']['CONN_MAX_AGE'] = 300

REDIS_URL = 'redis://localhost:6379'
REDIS_URL = os.getenv('REDIS_URL', REDIS_URL)
REDIS = urlparse.urlparse(REDIS_URL)

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

SECRET_KEY = '----------------- CHANGE ME --------------------'
# Set this to something valid, otherwise we have 500 Server Error. 
# DO NOT use '*' in production
ALLOWED_HOSTS = []
