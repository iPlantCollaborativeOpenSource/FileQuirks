import os
import sys

BASE_DIR = os.path.split(__file__)[0]
sys.path.append(os.path.split(BASE_DIR)[0])
sys.path.append(os.path.split(os.path.split(BASE_DIR)[0])[0])
os.environ['DJANGO_SETTINGS_MODULE'] = 'types_database.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

