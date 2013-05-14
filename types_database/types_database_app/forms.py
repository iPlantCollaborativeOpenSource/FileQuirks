# -*- coding: utf-8 -*-
from models import *
from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile

import re

class DataFileForm(forms.ModelForm):
    """
    Customized data file entry. Allows pasting data file from clipboard.
    """
    class Meta:
        model = DataFile
    paste = forms.CharField(required = False, widget = \
        forms.widgets.Textarea(attrs = {'cols': 80}))
    file = forms.FileField(required = False)
    def clean(self):
        """
        Check if only one of data entry methods was used. Create file if
        neccessary.
        """
        file = self.cleaned_data.get("file")
        paste = self.cleaned_data.get("paste")
        if file and not paste:
            pass
        elif paste and not file:
            number = DataFile.objects.all().count()
            self.cleaned_data["file"] = \
                SimpleUploadedFile("pasted-data", paste)
            del self.cleaned_data["paste"]
        else:
            raise forms.ValidationError( \
                "Please either specify file or paste data.")
        return self.cleaned_data


class RegexpForm(forms.ModelForm):
    """
    Regexp insertion form that validates regexp before addition.
    """
    class Meta:
        model = Regexp 
    def clean_content(self):
        """
        Try to compile regular expression.
        """
        content = self.cleaned_data.get("content")
        if content:
            try:
                re.compile(content)
            except:
                raise forms.ValidationError("Invalid regular expression.")
        return content

class CheckFileForm(forms.Form):
    """
    Form allowing to submit a file to check its type. File can be either
    pasted or selected from file system.
    """
    file = forms.FileField(required = False)
    paste = forms.CharField(max_length = 1000000, required = False, widget = forms.widgets.Textarea(attrs = {"cols": 60}))
    #expected_type_choice = forms.ChoiceField(required = False, choices = [])
    #expected_type = forms.CharField(max_length = 45, required = False)
    # only HTML is implemented
    # result_format = forms.ChoiceField(choices = ["HTML", "XML"])
    #do_not_store = forms.BooleanField(required = False)

    def __init__(self, *args, **kwargs):
        super(CheckFileForm, self).__init__(*args, **kwargs)
        # Initialize expected data type suggestions.
        #self.fields["expected_type_choice"].choices = [("", "---")] + \
            #[(type.name, type.name) 
            #for type in DataType.objects.order_by("name")]

    def clean(self):
        """
        Customized clean function. Ensures that certain fields are mutually
        exclusive.
        """
        file = self.cleaned_data.get("file")
        pasted = self.cleaned_data.get("paste")
        #type_choice = self.cleaned_data.get("expected_type_choice")
        #type_input = self.cleaned_data.get("expected_type")
        #do_not_store = self.cleaned_data.get("do_not_store")
        if file and not pasted:
            pass
        elif pasted:
            self.cleaned_data["file"] = SimpleUploadedFile("pasted", pasted.encode("utf-8"))
            del self.cleaned_data["paste"]
        else:
            raise forms.ValidationError( "The pasted data is empty")


        #fileContent = decode_file(form.cleaned_data["file"].read())
        if self.cleaned_data["file"].size>1000000:
            raise forms.ValidationError( "The pasted data is too big")
        #if not do_not_store and type_choice and type_input:
            #raise forms.ValidationError( \
                #"Please use only one method to specify the expected type.")
        #self.cleaned_data["expected_type"] = type_choice or type_input or ""
        return self.cleaned_data

class SubmitFileForm(forms.Form):
    """
    Form allowing to submit a file to check its type. File can be either
    pasted or selected from file system.
    """
    file = forms.FileField(required = False)
    paste = forms.CharField(max_length = 38000, required = False, widget = forms.widgets.Textarea(attrs = {"cols": 60}))
    expected_type_choice = forms.ChoiceField(required = False, choices = [])
    expected_type = forms.CharField(max_length = 45, required = False)
    # only HTML is implemented
    # result_format = forms.ChoiceField(choices = ["HTML", "XML"])
    #do_not_store = forms.BooleanField(required = False)

    def __init__(self, *args, **kwargs):
        super(SubmitFileForm, self).__init__(*args, **kwargs)
        # Initialize expected data type suggestions.
        self.fields["expected_type_choice"].choices = [("", "---")] + \
            [(type.name, type.name) 
            for type in DataType.objects.order_by("name")]

    def clean(self):
        """
        Customized clean function. Ensures that certain fields are mutually
        exclusive.
        """
        file = self.cleaned_data.get("file")
        pasted = self.cleaned_data.get("paste")
        type_choice = self.cleaned_data.get("expected_type_choice")
        type_input = self.cleaned_data.get("expected_type")
        #do_not_store = self.cleaned_data.get("do_not_store")
        if file and not pasted:
            pass
        elif pasted and not file:
            self.cleaned_data["file"] = \
                SimpleUploadedFile("pasted", pasted.encode("utf-8"))
            del self.cleaned_data["paste"]
        else:
            raise forms.ValidationError( \
                "Please either specify file or paste data.")
        if not (type_choice or type_input):
            print type_input
            raise forms.ValidationError( \
                "Please define the format of your data by selecting from a list or writing it.")
        if type_choice and type_input:
            raise forms.ValidationError( \
                "Please use only one method to specify the expected type.")
        self.cleaned_data["expected_type"] = type_choice or type_input or ""
        return self.cleaned_data

class SubmitRegexForm(forms.ModelForm):
    class Meta:
        model = SubmittedRegex
    content = forms.CharField(max_length = 180, required = True, \
        label = "Regular expression")
    description = forms.CharField(max_length = 540, required = True, \
        widget = forms.widgets.Textarea(attrs = {"cols": 60}))
    submitter_email = forms.CharField(max_length = 180, required = False, \
        label = "Email")
    def clean_content(self):
        """
        Try to compile submitted regular expression.
        """
        content = self.cleaned_data.get("content")
        if content:
            try:
                re.compile(content)
            except:
                raise forms.ValidationError("Invalid regular expression.")
        return content
