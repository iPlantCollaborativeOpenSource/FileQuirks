# -*- coding: utf-8 -*-
from django.db import models
from types_database.types_database_app.models import DataType
from types_database.types_database_app.storage import AutoNamingStorage
 
class SubmittedFile(models.Model):
    """
    Stores information about submitted file.
    """
    expected_type = models.CharField(max_length = 45, blank = True)
    date = models.DateField(editable = False)
    file = models.FileField(max_length = 180, upload_to = "submitted_files", \
        storage = AutoNamingStorage())
    results = models.ManyToManyField(DataType, through = 'SubmittedFileResult')
    def __unicode__(self):
        return self.file.name + " (" + self.expected_type + ")"


class SubmittedFileResult(models.Model):
    """
    Represents a type result (score) for file submitted by user.
    """
    file = models.ForeignKey(SubmittedFile)
    type = models.ForeignKey(DataType)
    score = models.FloatField()
    def __unicode__(self):
        return unicode(self.file) + ", " + unicode(self.type) + ": " \
            + str(self.score)
