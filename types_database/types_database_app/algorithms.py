# -*- coding: utf-8 -*-
"""
Algorithms module contains implementations of type-evaluating algorithms
and utility functions used by them.

Implementation of algorithm should take one parameter: results of regular
expression seatch on some text sorted by regexp primary key. Returned value
should be list of tuples: (type, type's score).
"""
from django.db import connection
from models import DataType, Regexp, ExpertRegex, DataFile
import re
import math
from django.core.urlresolvers import reverse
import numpy

class TypesBase(object):
    """
    Abstract base class containing type information.
    """
    def __init__(self):
        self.properties = {}
        self.datafilenumber={}
        for data_type in DataType.objects.all():
            self.properties[data_type.id] = {}
            self.datafilenumber[data_type.id] = 0

    def type_vector(self, data_type_id):
        """
        Return list [t(1), t(2), ..., t(n)] where t(i) is percentage of files in
        given type matching regular expression i.
        """
        result= [float(value) for value in self.properties[data_type_id].values()]
        #sys.stderr.write(str(result)+"\n")
        return result

class Types(TypesBase):
    """
    Simple implementation of type information object.
    """
    def __init__(self):
        super(Types, self).__init__()
        query = """SELECT P.regexp_id, SUM(`match`), R.weight
            FROM types_database_app_datafileproperty P 
            JOIN types_database_app_datafile F 
            ON P.data_file_id = F.id
            JOIN types_database_app_regexp R 
            ON P.regexp_id = R.id 
            WHERE F.data_type_id = ???
            GROUP BY P.regexp_id 
            ORDER BY P.regexp_id"""
        filenumber_query="SELECT COUNT(*) FROM types_database_app_datafile WHERE data_type_id=??? GROUP BY data_type_id ORDER BY data_type_id"
        for data_type in DataType.objects.all():
            cursor = connection.cursor()
            cursor.execute(query.replace("???", str(data_type.id)))
            cursor2 = connection.cursor()
            cursor2.execute(filenumber_query.replace("???", str(data_type.id)))
            for row in cursor.fetchall():
                self.properties[data_type.id][row[0]] = row[1]*row[2]
            for row in cursor2.fetchall():
                self.datafilenumber[data_type.id] = row[0]
            

def normalize(vector):
    """
    Changes vector's length to 1 if it is nonzero.
    """
    vector_length = math.sqrt(reduce(lambda x, y: x + y ** 2, vector, 0))
    return vector if vector_length == 0 else [x / vector_length for x in
        vector]

def dot_product(vector_1, vector_2):
    """
    Dot product of two iterables of equal length.
    """
    return reduce(lambda x, y: x + y, map(lambda x, y: x * y if x else 0.0, vector_1, vector_2), 0.0)

#def algo2(vector_1, vector_2):
    ##vector2_norm2=normalize(vector_1)
    #r1=0.0
    #r2=0.0
    #l1=0.0
    #l2=0.0
    #l=float(len(vector_1))
    #ll=float(len(vector_2))
    #if l!=ll:
        #raise Exception,"lengts not equal"
    #for i in range(len(vector_2)):
        #if vector_2[i]==0:
            #r1=r1+vector_1[i]
            #l1=l1+1.0
        #elif vector_2[i]==1:
            #r2=r2+vector_1[i]
            #l2=l2+1.0
        #else:
            #raise Exception,"Incorrect vector value"
    #rr1=float(r1)/l1
    #rr2=float(r2)/l2
    #rr3=l2/float(len(vector_1))
    #return [rr1,rr2,rr3]
    
def text_vector(text):
    """
    Returns list [v(1), v(2), ..., v(n)], where v(i) is result of regular
    expression i on a given text.
    """
    result=[]
    for regex in Regexp.objects.order_by("id"):
        result.append(regex.match(text))
    return result
    #return [1*regex. if re.compile(regex.content, re.M).search(text) else 0 for regex in Regexp.objects.order_by("id")]

def check_type_products(input_vector, types = Types()):
    """
    Return a list of tuples: (type, type's score) for each type.
    """
    input_vector = normalize(input_vector) 
    return [(file_type, dot_product(normalize(types.type_vector(file_type)), input_vector)) for file_type in types.properties.keys()]

def check_type_products2(input_vector, types = Types()):
    """
    Return a list of tuples: (type, type's score_1,type_score_2,type_score_3,type_score_4) for each type.
    """
    input_vector_norm = normalize(input_vector)
    #print input_vector_norm
    #print 
    #print

    results=[]
    for file_type in types.properties.keys():
        if types.datafilenumber[file_type]>0:
            type_vector=types.type_vector(file_type)
            dot_product_result=dot_product(normalize(type_vector),input_vector_norm)
            #if file_type==19 or file_type==97:
                #print normalize(type_vector)
            #result_vector=algo2(type_vector,input_vector)
            #result=(file_type, dot_product_result, result_vector[0],result_vector[1],result_vector[2])
            result=[file_type, dot_product_result]
            results.append(result)
    #add z_value
    results2=[]
    values=[]
    for result in results:
        values.append(result[1])
    avg=numpy.average(values)
    std=numpy.std(values)
    for result in results:
        z_value=0.0
        if std!=0.0:
            z_value=(result[1]-avg)/std
        if math.isnan(z_value):
            raise Exception("nan: result=%s avg=%s std=%s" %(result,avg,std))
        result.append(z_value)
        
    return results

def prop(i1,i2):
    """
    Return a probablity that the hit is correct from hit number and first of scores using linear logistic regression
    """
    return 1/(1+math.e**-(-33.936+15.268*i1+23.000*i2))

def prop2(i1,i2,i3,i4,i5):
    """
    Return a probablity that the hit is correct from hit number and all scores using linear logistic regression
    can be used only with scores generated by check_type_products2 function
    """
    return 1/(1+math.e**-(-39.607+14.632*i1+33.451*i2+43.984*i3-4.416*i4))

def quality_function(index):
    """
    Returns a score between 0 and 1 for position of hit on the list.
    1 - first
    0 - very far
    """
    index=float(index)
    k=4.0
    return 1.0 / (1.0 + (index/k)**2)

def check_expert_types(fileContent):
    result=[]
    for expert_regex in ExpertRegex.objects.all():
        match=expert_regex.match(fileContent)
        if match:
            example_file=DataFile.objects.filter(data_type=expert_regex.data_type)[0]
            url="display_match/%d/%d" %(expert_regex.id,example_file.id)
            result.append([expert_regex,match,example_file,url])
    return result
