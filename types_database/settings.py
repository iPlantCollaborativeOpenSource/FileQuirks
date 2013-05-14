# -*- coding: utf-8 -*-
# Django settings for types_database project.

import os.path

BASE_DIR = os.path.split(__file__)[0]

# This is the base URL of the application
URL_PREFIX = ''
URL_PREFIX2 = ''
#Uncomment this when using Apache:
#URL_PREFIX2 = ''

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'

DATABASE_NAME = 'TypesDB'

DATABASE_USER = 'app'
DATABASE_PASSWORD = 'w00tums'
DATABASE_HOST = '127.0.0.1'    # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = '3306'         # Set to empty string for default. Not used with sqlite3.
DATABASE_OPTIONS = {"init_command": "SET storage_engine=INNODB"}

# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Warsaw'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(BASE_DIR, '../media')

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = 'data_file_view'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = URL_PREFIX + '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'bi-$$1xww6tn#f_%dlqwosh+l2$z&ccdkinye5b=(x2)6#repd'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'types_database.urls'

TEMPLATE_DIRS = [
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'templates')
]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'types_database.types_database_app',
    'types_database.file_log'
)

LOGIN_URL = URL_PREFIX + '/login/'

TEMPLATE_CONTEXT_PROCESSORS=(
    'types_database.types_database_app.custom_context_processors.name',
    'django.core.context_processors.auth',
)
