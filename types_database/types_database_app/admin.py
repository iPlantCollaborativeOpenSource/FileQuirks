# -*- coding: utf-8 -*-
"""
This module registers types database application models in the admin panel.
"""
from django.contrib.auth.models import User, Group
from models import Keyword, DataType, DataFile, DataFileProperty, Regexp, \
    ExpertRegex, SubmittedRegex
from django import forms
from django.contrib import admin
from django.db import models


admin.site.register(Keyword)
admin.site.register(DataType)

class MyDataFileAdminForm(forms.ModelForm):
    class Meta:
        model = DataFile


class DataFileAdmin(admin.ModelAdmin):
    #pass
    form = MyDataFileAdminForm
    #exclude = ('data_type',)




admin.site.register(DataFile, DataFileAdmin)


admin.site.register(DataFileProperty)
admin.site.register(Regexp)

admin.site.register(User)
admin.site.register(Group)
admin.site.register(ExpertRegex)
admin.site.register(SubmittedRegex)

