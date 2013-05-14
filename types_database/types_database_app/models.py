# -*- coding: utf-8 -*-
"""
Types database models.
"""
from django.db import models
from storage import AutoNamingStorage
from text import decode_file
import re
from django.core.exceptions import ValidationError

REGEXP_TYPE_CHOICES = (
    ('search', 'search'),
    ('match', 'match'),
)


class Keyword(models.Model):
    """
    Allows classification of data files. Currently unused.
    """
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length = 45, unique = True)


class Regexp(models.Model):
    """
    Stores regular expression code with name.
    """
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length = 45)
    content = models.CharField(max_length = 180, blank = True)
    weight= models.PositiveIntegerField(default=1)
    regexp_type=models.CharField(max_length=20, default='search', choices=REGEXP_TYPE_CHOICES)

    def process(self):
        """
        Evaluates given regex for each data file and stores results in the DB.
        """
        # I expect all regexps in DB to be validated.
        for data_file in DataFile.objects.all():
            text = decode_file(data_file.file.read())
            data_file.file.close()
            update_property(data_file, self, text)

    def save(self, force_insert = False, force_update = False):
        """
        Customized save. Triggers result recalculation after update.
        """
        super(Regexp, self).save(force_insert, force_update)
        self.process()

    def match(self,text):
        result=0
        r=re.compile(self.content, re.M)
        if self.regexp_type=='search':
            if r.search(text):
                result=self.weight
        elif self.regexp_type=='match':
            m= r.match(text)
            if m:
                if len(m.group())==len(text):
                    result=self.weight
        else:
            raise Exception,"unknown regexp_type: %s" %(self.regexp_type)
        return result


class DataType(models.Model):
    """
    Information about data type.
    """
    def __unicode__(self):
        return "%d : %s" %(self.id,self.name)

    name = models.CharField(max_length=45, unique = True)
    description = models.CharField(max_length = 180, blank = True)
    keywords = models.ManyToManyField(Keyword, blank = True)
    category = models.CharField(max_length = 180, blank = True, null=True)

class DataFile(models.Model):
    """
    Stores information about data file. File is represented as path.
    """
    def __unicode__(self):
        return "Data file #" + self.pk.__str__() + " (" + \
            self.data_type.name + " @ " + self.file.name + ")"
     
    data_type = models.ForeignKey(DataType);
    keywords = models.ManyToManyField(Keyword, blank = True)
    properties = models.ManyToManyField(Regexp, through = 'DataFileProperty')
    file = models.FileField(max_length = 180, upload_to = 'data_files', \
         storage = AutoNamingStorage())

    def process(self):
        """
        Try all regexps on particular data_file. Stores results in DB.
        """
        self.file.file.open()
        text = decode_file(self.file.file.read())
        self.file.file.close()
        [update_property(self, regexp, text)
            for regexp in Regexp.objects.all()]

    def save(self, force_insert=False, force_update=False):
        """
        Modified save method. Removes old file after update and updates
        data type's properties.
        """
        
        expert_regexes=ExpertRegex.objects.filter(data_type=self.data_type)
        self.file.file.open()
        text = decode_file(self.file.read())
        self.file.file.close()
        for regex in expert_regexes:
            if ( not regex.match(text)):
                raise ValidationError, "File does not match all regular expressions of its type"
             

        if self.pk:
            try:
                old_object = DataFile.objects.get(pk = self.pk)
                if old_object.file.path != self.file.path:        
                    path = old_object.file.path
                    print "Old pk: " + self.pk.__str__()
                    print "Deleting: " + path
                    old_object.file.storage.delete(path)
            except self.DoesNotExist:
                pass
        super(DataFile, self).save(force_insert, force_update)
        self.process()


class DataFileProperty(models.Model):
    """
    Result of regular expression search on file. Adding Regex or DataFile
    automatically creates DataFileProperty objects.
    """
    regexp = models.ForeignKey(Regexp)
    data_file = models.ForeignKey(DataFile)
    match = models.BooleanField()
    def __unicode__(self):
        return self.data_file.__unicode__() + " -- "+ self.regexp.name + \
            (" +" if self.match else " -")
    class Meta:
        verbose_name_plural = "data files' properties"

def update_property(data_file, regexp, text):
    #print data_file
    """
    Match regexp and store result in DB. Assumes that r is compiled regexp
    content and text is data_file.file content.
    """
    match_int=regexp.match(text)
    match=match_int>0
    #compiled_regexp = re.compile(regexp.content, re.M)
    #match = True if compiled_regexp.search(text) else False
    try:
        p = DataFileProperty.objects.get(data_file = data_file, \
            regexp = regexp)
        p.match = match
        p.save()
    except:
        p = DataFileProperty.objects.create(data_file = data_file, \
            regexp = regexp, match = match)

def rebuild_properties():
    """
    Deletes all old DataFileProperties and calculates new ones as if database
    was created from scratch.
    """
    DataFileProperty.objects.all().delete()
    [regexp.process() for regexp in Regexp.objects.all()]

class ExpertRegex(models.Model):
    """
    Expert regular expressins that match only one data type
    """
    def __unicode__(self):
        return self.name    

    name = models.CharField(max_length = 45, unique=True)
    data_type=models.ForeignKey(DataType)
    content = models.CharField(max_length = 180)
    regexp_type=models.CharField(max_length=20, default='search', choices=REGEXP_TYPE_CHOICES)

    def clean(self):
        if not self.name:
            raise ValidationError, "name needed for expert regular expression" 
        if not self.content:
            raise ValidationError, "name needed for expert regular expression"
        for data_file in DataFile.objects.filter(data_type=self.data_type):
            text = decode_file(data_file.file.read())
            if ( not self.match(text)):
                raise ValidationError, "Expert regular expression does not match all files of its connected type\n  file:%s\n  regex:%r" %(data_file.file.path,self.content )
            
    def match(self,text):
        result=0
        m=None
        r=re.compile(self.content, re.M)
        if self.regexp_type=='search':
            m=r.search(text)
            if m:
                result=1
        elif self.regexp_type=='match':
            m= r.match(text)
            if m:
                if len(m.group())==len(text):
                    result=1
        else:
            raise Exception,"unknown regexp_type: %s" %(self.regexp_type)
        if result:
            return [result,m]
        else:
            return []
        

    def save(self, force_insert = False, force_update = False):
        self.clean()
        super(ExpertRegex,self).save(force_insert,force_update)

        
        
class SubmittedRegex(models.Model):
    """
    Regular expression submitted by a user.
    """
    content = models.CharField(max_length = 180, blank = False)
    date = models.DateTimeField(auto_now_add = True, editable = False)
    description = models.CharField(max_length = 540, blank = True)
    submitter_email = models.CharField(max_length = 180, blank = True)

