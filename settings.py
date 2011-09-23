try:
    # Try to load production settings, if any...
    from config.production_settings import *
    print "Using production settings."
except ImportError:
    # Make sure this file exists in development
    from config.local_settings import *
    print "Using local settings."
