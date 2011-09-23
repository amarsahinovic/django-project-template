from django.conf.urls.defaults import *
from app1 import views

urlpatterns = patterns('',
    (r'^$', views.index),
)
