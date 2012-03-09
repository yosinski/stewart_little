from django.conf.urls.defaults import *

from main.models import *
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',       'main.views.static', {'page': 'main/index.html'}, name='index'),
)

if settings.SERVE_STATIC:
    urlpatterns += patterns('',
        # Static serve for development
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )

handler404 = 'main.views.handler404'
handler500 = 'main.views.handler500'
