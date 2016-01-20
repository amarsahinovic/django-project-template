from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$',
        views.HomepageView.as_view(),
        name='homepage',),
]
