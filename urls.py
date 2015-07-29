from django.conf.urls import patterns, url, include

from main.models import *
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',       'main.views.static', {'page': 'main/index.html'}, name='index'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

handler404 = 'main.views.handler404'
handler500 = 'main.views.handler500'
