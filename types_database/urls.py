# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include
from django.contrib.auth.views import login
from types_database_app.admin import admin
import file_log.admin
from settings import URL_PREFIX2
# Comment this out if you use Apache
from settings import MEDIA_ROOT
import os.path

from django.conf.urls.defaults import *


urlpatterns = patterns('',
    (r'^'+URL_PREFIX2+r'admin_panel/(.*)', admin.site.root),
    (r'^'+URL_PREFIX2+r'admin_menu/$', 'types_database.types_database_app.views.index'),
    (r'^'+URL_PREFIX2+r'', include('types_database.types_database_app.urls')),
    (r'^'+URL_PREFIX2+r'login/', 'django.contrib.auth.views.login',{'template_name': 'login.html'}),
    # Comment this out if you use Apache
    (r'^'+URL_PREFIX2+r'site-media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(MEDIA_ROOT, "../site")}),
)
