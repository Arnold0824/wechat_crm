from django.shortcuts import render
#from core.models import TASK,USER,CPN,CLM,CLMLST
from core.models import *
from django.http import HttpResponse, HttpResponseRedirect
#from PIL import Image,ImageDraw,ImageFont
from math import ceil
import random
import os
import io as cStringIO
from datetime import datetime
import hashlib
from django.core.files.storage import default_storage
import json
import time
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import connection
from django.utils import timezone
try:
    from functools import wraps
except ImportError:
    from django.utils.functional import wraps  # Python 2.4 fallback.
from django.utils.decorators import available_attrs
import base64
from pyDes import *
import urllib.parse
import urllib
import sys
import http.cookiejar
import json


def my_custom_sql(sql,*para):
    cursor = connection.cursor()

    cursor.execute(sql,*para)

    #cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
    row = cursor.fetchall()

    return row
def sign(s):#签名加密方式
    k = des("mv03nd.f", ecb, "\0\0\0\0\0\0\0\0",
                pad=none, padmode=pad_pkcs5)
    return base64.b64encode(k.encrypt(s))
def post(url, data):#封装post方法
    return urllib.request.urlopen(url, urllib.parse.urlencode(data).encode('utf-8')).read()
def index(request):
    return render(request,'index.html',locals())

