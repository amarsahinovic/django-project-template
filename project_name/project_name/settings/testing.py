from .base import *

print 'Using testing settings'

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.sqlite3',
        'NAME':     '',
        'USER':     '',
        'PASSWORD': '',
        'HOST':     '',
        'PORT':     '',
    }
}

TEST_RUNNER = 'aftermath.AftermathTestRunner'
# Uncomment this to use notify-send backend. 
# By default, it uses NullBackend which does nothing
#AFTERMATH_BACKEND = 'aftermath.backends.NotifySendBackend'

STATIC_URL = '/static/'
