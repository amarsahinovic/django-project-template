from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url

import views

urlpatterns = patterns('',

    url(r'^$',
        views.HomepageView.as_view(),
        name='homepage',),
)
