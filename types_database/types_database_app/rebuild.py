from types_database.types_database_app.models import DataFile, \
     DataFileProperty, Regexp
import re

def add_property(data_file, regexp):
    """
    Match regexp and store result in DB. Assumes that r is compiled regexp
    content.
    """
    if regexp.match(data_file.file.read()):
        match = True
    else:
        match = False
    data_file.file.close()
    try:
        p = DataFileProperty.objects.get(data_file = data_file, \
            regexp = regexp)
        p.match = match
        p.save()
    except:
        p = DataFileProperty.objects.create(data_file = data_file, \
            regexp = regexp, match = match)

def remove_property(data_file, r, regexp):
    """
    Reverse add_property.
    """
    if r.match(data_file.file.read()):
        p = DataFileProperty.objects.get(data_type = \
            data_file.data_type, regexp = regexp)
        if p.weight == 1.0:
	    p.delete()
        else:
            p.weight -= 1.0
            p.save()

def process_regexp(regexp):
    """
    Evaluates given regexp for each data file and stores results in the DB.
    """
    # I expect all regexps in DB to be validated.
    r = re.compile(regexp.content)
    [add_property(data_file, regexp) \
        for data_file in DataFile.objects.all()]

def unprocess_regexp(regexp):
    """
    Evaluates given regexp for each data_file and removes results from DB.
    """
    r = re.compule(regex.content)
    [remove_property(data_file, r, regexp) \
        for data_file in DataFile.objects.all()]

def process_data_file(data_file):
    """
    Try all regexps on particular data_file. Stores results in DB.
    """
    [add_property(data_file, re.compile(regexp.content), regexp) \
        for regexp in Regexp.objects.all()]

def unprocess_data_file(data_file):
    """
    Reverse process_data_file function.
    """
    [remove_property(data_file, re.compile(regexp.content), regexp) \
        for regexp in Regexp.objects.all()]

def rebuild_properties():
    """
    Rebuild contents of DataFileProperty model. Fist, it erases all old data.
    Then it scans all data files with all regexps and saves new results.
    Implemented using process_regexp function.
    """   
    DataFileProperty.objects.all().delete()
    [process_regexp(regexp) for regexp in Regexp.objects.all()]
    return 1

