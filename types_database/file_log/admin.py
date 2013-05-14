"""
This module registers file logger models in the admin panel.
"""
from django.contrib.admin import site
from django.contrib.auth.models import User, Group
from models import SubmittedFile, SubmittedFileResult

site.register(SubmittedFile)
site.register(SubmittedFileResult)
