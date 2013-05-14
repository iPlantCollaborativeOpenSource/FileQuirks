# -*- coding: utf-8 -*-
"""
Views used by FileQuirks main application.
"""
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.admin import site as admin_site
from forms import CheckFileForm, SubmitFileForm, SubmitRegexForm
from storage import AutoNamingStorage
from django.core.files.storage import FileSystemStorage
from types_database.settings import MEDIA_ROOT, URL_PREFIX2
from django.shortcuts import render_to_response
from models import *
from text import decode_file
from django.template import RequestContext
from django.core.urlresolvers import reverse

import math
import os
import algorithms
import re
import datetime
import file_log.models
import subprocess
import time
import json

"""
Global variables
"""
#TRID_PATH = "C:/Documents and Settings/aa/Pulpit/filequirks/filequirks/1.0-rc2/types_database/types_database_app/TRID/trid"

TRID_PATH = os.path.join(os.path.split(os.path.split(os.path.split(__file__)[0])[0])[0],"trid")
TRID_EXECUTABLE_PATH=os.path.join(TRID_PATH,"trid")
TRID_LIBRARY_PATH=os.path.join(os.path.join(TRID_PATH,"defs"),"TrIDDefs.TRD")

def classify_score2(score):
    """
    Convert score to one of 6 classes: mark_0 to mark_5.
    """
    if score<=2.0:
        return "mark_5"
    elif score<=2.5:
        return "mark_4"
    elif score<=3.0:
        return "mark_3"
    elif score<=4.0:
        return "mark_2"
    else:
        return "mark_1"

def classify_score(score):
    """
    Convert score to one of 6 classes: mark_0 to mark_5.
    """
    if score<0.00001:
      return "mark_5"
    return "mark_" + str(int(round(-math.log(score,10)-0.18)))

def index(request):
    """
    View showing menu of application functions.
    """
    template = loader.get_template('index.xhtml')
    context = Context({})
    return HttpResponse(template.render(context))

def do_check(form):
    """
    Gathers information about a submitted file.
    """
    if form.is_valid():
        fileContent = decode_file(form.cleaned_data["file"].read())
        if not fileContent:
            new_file = file_log.models.SubmittedFile()
            new_file.date = datetime.date.today()
            new_file.file.save(form.cleaned_data["file"].name, \
                form.cleaned_data["file"])
            new_file.save()
            return do_binary_check(request, new_file)
        
        text_vector = algorithms.text_vector(fileContent)
        results = algorithms.check_type_products2(text_vector)
        expert_results=algorithms.check_expert_types(fileContent)
        #save file in log:
        new_file = file_log.models.SubmittedFile()
        #new_file.expected_type = form.cleaned_data["expected_type"]
        new_file.date = datetime.date.today()
        form.cleaned_data["file"].open()
        new_file.file.save(form.cleaned_data["file"].name, \
            form.cleaned_data["file"])
        new_file.save()
        for result in results:
            new_result = file_log.models.SubmittedFileResult()
            new_result.file = new_file
            new_result.type = DataType.objects.get(id = result[0])
            new_result.score = result[1]
            new_result.save()
        # postprocess the results: sort, round and add classification
        results.sort(key = lambda x: x[1], reverse = True)
        results2=[]
        for i in range(len(results)):
            x=results[i]
            
            scorestring=0


            dataType=DataType.objects.get(id = x[0])
            example_file=DataFile.objects.filter(data_type=dataType)[0]
            results2.append((dataType.name, 
                             round(x[1], 3),
                             classify_score2(x[2]), 
                             int(x[1] * 200),
                             scorestring,
                             example_file,
                             round(x[2], 3)))
            results2=results2[0:20]
        return {"text_content": True, "result": results2,
            "fileContent": fileContent[0:100000],
             "expert_results": expert_results, "new_file": new_file}
    else:
        return None

def do_binary_check(new_file):
    """
    Gathers information about a bad (binary) file.
    """
    path = new_file.file.path
    ExecFile = subprocess.Popen([TRID_EXECUTABLE_PATH,"-d:%s" %(TRID_LIBRARY_PATH),
                                 path],
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
    ExecFile.wait()
    Output = ExecFile.stdout.read()
    OutputList = Output.split("\n")
    OutputList2 = OutputList[6:len(OutputList)-2]
    return {"text_content": False, "result": OutputList2}

def check(request):
    """
    This view displays check file form and also saves results of submitted
    files.
    """
    if request.method == "POST":
        form = CheckFileForm(request.POST, request.FILES)
        output = do_check(form)
        if output:
            if output["text_content"]:
                result = output["result"]
                fileContent = output["fileContent"]
                expert_results = output["expert_results"]
                new_file = output["new_file"]
                return render_to_response("results.xhtml", {"result": result,
                    "fileContent": fileContent, "expert_results": expert_results,
                    "new_file":new_file},
                    context_instance = RequestContext(request))
            else:
                return render_to_response("bad_file.xhtml",
                    {'Output': output["result"]},
                    context_instance = RequestContext(request))
    else:
        form = CheckFileForm()
    return render_to_response("check.xhtml", {"form": form}, context_instance=RequestContext(request) )


"""
TODO
"""
def check_json(request):
    if request.method != "POST":
        return HttpResponse(status = 400)
    form = CheckFileForm(request.POST, request.FILES)
    output = do_check(form)
    if output == None:
        return HttpResponse(status = 400)
    if output["text_content"]:
        expert_result = [(r[0].data_type.name, URL_PREFIX2 + r[2].file.name, URL_PREFIX2 + r[3]) for r in output["expert_results"]]
        result = [(r[0], r[1], r[6]) for r in output["result"]]
        json_data = {"file_type": "text", "expert_result": expert_result,
            "result": result, "file_content": output["fileContent"]}
    else:
        json_data = {"file_type": "binary", "result": output["result"]}
    json_string = json.dumps(json_data)
    response = HttpResponse(json_string, mimetype = "application/json")
    return response

def submit_regex(request):
    if request.method == "POST":
        form = SubmitRegexForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            description = form.cleaned_data["description"]
            email = form.cleaned_data["submitter_email"]
            SubmittedRegex.objects.create(content = content, \
                description = description, submitter_email = email)
            return render_to_response("submitted_regex.xhtml", context_instance = RequestContext(request))
    else:
        form = SubmitRegexForm()
    return render_to_response("submit_regex.xhtml", {"form":  form}, context_instance = RequestContext(request))

def types(request):
    """
    Show a list of types.
    """
    data_types_list = DataType.objects.all()
    #template = loader.get_template('types.xhtml')
    #context = Context()
    #return HttpResponse(template.render(context))
    return render_to_response("types.xhtml", {'data_types_list': data_types_list}, context_instance=RequestContext(request) )

def regexp_table(request):
    """
    Renders a table of results of regular expression search on files int the
    database. This view requires login.
    """
    if not request.user.is_authenticated():
        return admin_site.login(request)
    data_dictionary={"data_files": [{"name": data_file.file.name, "properties": [property.match for property in DataFileProperty.objects.filter(data_file = data_file)]} for data_file in DataFile.objects.all()], 
                     "regexps": [regexp.name for regexp in Regexp.objects.all()]}
    #template = loader.get_template('regexp_table.xhtml')
    #return HttpResponse(template.render(context))
    return render_to_response("regexp_table.xhtml", data_dictionary, context_instance=RequestContext(request) )


def data_file_view(request, file_path):
    """
    Shows contents of file from the database. This view requires login.
    """
    storage = AutoNamingStorage()
    return HttpResponse(storage.open(file_path).read(), mimetype="text/plain")


def feedback_table(request):
    """
    Renders table of check-type results of files from the database.
    """
    if not request.user.is_authenticated():
        return admin_site.login(request)
    # Get data types from db
    data_types = [data_type.name for data_type in DataType.objects.all()]
    # Make list of tuples (file, type name, [(type_name, mark, score)])
    
    feedback_results = [(data_file.file, data_file.data_type.name,
        [(round(score[1], 3), classify_score(score[1]),
          DataType.objects.get(id = score[0]).name)
        for score in algorithms.check_type_products(\
           algorithms.text_vector(data_file.file.read()))])
        for data_file in DataFile.objects.all()]
    context = {"results": feedback_results, "data_types": data_types}
    return render_to_response("feedback_table.xhtml", context, context_instance=RequestContext(request))

def submit_file(request):
    """
    This view displays check file form and also seves results of submitted
    files.
    """
    
    if request.method == "POST":
        form = SubmitFileForm(request.POST, request.FILES)
        if form.is_valid():
            fileContent = decode_file(form.cleaned_data["file"].read())
            if not fileContent:
                #new_file = file_log.models.SubmittedFile()
                #new_file.date = datetime.date.today()
                #new_file.file.save(form.cleaned_data["file"].name, \
                    #form.cleaned_data["file"])
                #new_file.save()
                
                return bad_file2(request)
            
            text_vector = algorithms.text_vector(fileContent)
            #results = algorithms.check_type_products2(text_vector)
            #results = algorithms.check_type_products2(text_vector)
            # if "Do not store" wasn't checked, save file in log:
            if True:
                new_file = file_log.models.SubmittedFile()
                new_file.expected_type = form.cleaned_data["expected_type"]
                new_file.date = datetime.date.today()
                form.cleaned_data["file"].open()
                new_file.file.save(form.cleaned_data["file"].name, \
                    form.cleaned_data["file"])
                new_file.save()
                #for result in results:
                    #new_result = file_log.models.SubmittedFileResult()
                    #new_result.file = new_file
                    #new_result.type = DataType.objects.get(id = result[0])
                    #new_result.score = result[1]
                    #new_result.save()
            # postprocess the results: sort, round and add classification
            #results.sort(key = lambda x: x[1], reverse = True)
            #results2=[]
            #for i in range(len(results)):
                #x=results[i]
                #i_score=algorithms.quality_function(i)
                ##print x
                ##score=algorithms.prop2(i_score,x[1],x[2],x[3],x[4])
                #score=algorithms.prop(i_score,x[1])
                #scorestring=""
                #if score>=0.001:
                    #scorestring="%.3f" %(round(score,3))
                #else:
                    #scorestring="%.3e" %(score)
                #confident=0
                #if score>0.5:
                  #confident=1
                #results2.append((DataType.objects.get(id = x[0]).name, round(x[1], 3),classify_score(score), int(x[1] * 200),scorestring,confident))
                #results2=results2[0:20]

            return render_to_response("thankYou.xhtml", {} ,context_instance=RequestContext(request))
    else:
        form = SubmitFileForm()
    #template = loader.get_template('')
    #context = Context()
    return render_to_response("submitFile.xhtml", {"form": form}, context_instance=RequestContext(request) )


def display_match(request,expert_regex_id,data_type_id,data_file_id):
    regex=ExpertRegex.objects.get(id=expert_regex_id)
    user_data=file_log.models.SubmittedFile.objects.get(id=data_file_id)
    data=DataFile.objects.get(id=data_type_id)
    f1=user_data.file.read()
    f2=data.file.read()
   
    m1=regex.match(f1)[1]
    m2=regex.match(f2)[1]
    html_text1_1=html_escape(f1[0:m1.start()][-50000:])
    html_text1_2=html_escape(f1[m1.start():m1.end()][0:100000])
    html_text1_3=html_escape(f1[m1.end():][0:50000])
    html_text2_1=html_escape(f2[0:m2.start()][-50000:])
    html_text2_2=html_escape(f2[m2.start():m2.end()][0:100000])
    html_text2_3=html_escape(f2[m2.end():][0:50000])
    
    
    return render_to_response("display_match.xhtml", 
                                {"text1":f1,
                                "html_text1_1":html_text1_1,
                                "html_text1_2":html_text1_2,
                                "html_text1_3":html_text1_3,
                                "text2":f2,
                                "html_text2_1":html_text2_1,
                                "html_text2_2":html_text2_2,
                                "html_text2_3":html_text2_3,
                                "data":data}, 
                                context_instance=RequestContext(request) )

def data_file_view2(request,file_id):
    data=DataFile.objects.get(id=file_id)
    f2=data.file.read()
    return render_to_response("display_file2.xhtml", 
                            {"data":f2}, 
                            context_instance=RequestContext(request),
                            mimetype="text/plain")

def data_types_view(request,category,file_type=0):
    types=DataType.objects.all()
    types_dict={}
    for type in types:
        category = type.category or ""
        if types_dict.has_key(category):
            types_dict[category].append(type)
        else:
            types_dict[category]=[type]
    types_dict2=[]
    for key in types_dict.keys():
        key2=key
        if key=="":
            key2="other"
        if key2==category:
            types_dict2.append([key2,types_dict[key]])
        else:
            types_dict2.append([key2,[]])
    
    file_type=int(file_type)
    files=[]
    if file_type>0:
        data_type_s=DataType.objects.get(id=file_type)
        files=DataFile.objects.filter(data_type=data_type_s)

    return render_to_response("display_types.xhtml", 
                                {"types_dict":types_dict2,"files":files,"file_type":file_type}, 
                                context_instance=RequestContext(request) )

def json_info(request):
  return render_to_response("json_info.xhtml", {}, context_instance=RequestContext(request))


html_escape_table = [
    ["&", "&amp;"],
    ['"', "&quot;"],
    ["'", "&apos;"],
    [">", "&gt;"],
    ["<", "&lt;"],
    ["\n","<br/>"],
    ]

def html_escape(text):
    """Produce entities within text."""
    for replace in html_escape_table:
        text=text.replace(replace[0],replace[1])
    return text





    
    
    
