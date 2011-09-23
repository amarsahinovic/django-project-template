from django.conf.urls.defaults import *
from core import views

urlpatterns = patterns('',
    (r'^$', views.index),
)
