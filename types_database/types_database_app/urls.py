# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'types_database.types_database_app.views.check'),
    (r'^json/$', 'types_database.types_database_app.views.check_json'),
    (r'^json_info/$', 'types_database.types_database_app.views.json_info'),
    (r'^submit_file/$', 'types_database.types_database_app.views.submit_file'),
    (r'^submit_regex/$', 'types_database.types_database_app.views.submit_regex'),
    (r'^types/.*$', 'types_database.types_database_app.views.types'),
    (r'^regexp_table/.*$', \
        'types_database.types_database_app.views.regexp_table'),
    (r'^feedback_table/.*$', \
        'types_database.types_database_app.views.feedback_table'),
    (r'^data_file_view/(?P<file_path>.*)$', \
        'types_database.types_database_app.views.data_file_view'),
    (r'^display_match/(?P<expert_regex_id>\d+)/(?P<data_type_id>\d+)/(?P<data_file_id>\d+)$', \
        'types_database.types_database_app.views.display_match'),
    #(r'^data_types/$', \
        #'types_database.types_database_app.views.data_types_view'),
    (r'^data_types/(?P<category>[^/]*)$', \
        'types_database.types_database_app.views.data_types_view'),
    (r'^data_types/(?P<category>[^/]+)/(?P<file_type>\d+)$', \
        'types_database.types_database_app.views.data_types_view'),
    (r'^data_file_view2/(?P<file_id>\d+)$', \
        'types_database.types_database_app.views.data_file_view2'),
)
