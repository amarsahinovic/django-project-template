from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import include
from django.conf.urls.defaults import url
from django.conf.urls.static import static
from django.conf import settings


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
    (r'^app1/',    include('apps.app1.urls')),
    # Add your apps here
)


# Following two settings are for serving static files in development, 
# and are only active if DEBUG = True
# Static files, from static/ directory
urlpatterns += staticfiles_urlpatterns()
# Media files, from media/ directory
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Root of the website, needs to be last and added like this
# We can't use (r'^/', include('apps.core.urls')) for root because this will not
# work for homepage, where url is basically '', and we are trying to capture '/' url, 
import apps.core.urls
urlpatterns += apps.core.urls.urlpatterns

