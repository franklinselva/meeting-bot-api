# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.core.files import utils
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
import subprocess
import sys

from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

from subprocess import run, PIPE
import sys

from app.utils.transcriber import transcribe_gcs


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/franklinselva/Documents/freelancing/meeting-bot-api/config/service-client-rk.json"
transcribedFile = None

@login_required(login_url="/login/")
def results(request):
    context = {}
    context['segment'] = 'index'
    
    if transcribedFile is not None:
        module_dir = os.path.dirname(__file__)  
        file_path = os.path.join(module_dir, 'test.txt')   #full path to text.
        data_file = open(file_path , 'r')       
        data = data_file.read()
        context = {'data': data}
        return render(request, 'core/results.html',context)
    else:
        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))
    
    
@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def transcribe(request):
    """ Enables the transcribing part from video to text

    Args:
        directory ([string]): [Give the directory of the video file]
    """
    video=request.FILES['video']
    # print("video is ",video)
    fs=FileSystemStorage()
    filename=fs.save(video.name,video)
    fileurl=fs.open(filename)
    templateurl=fs.url(filename)
    # print("file raw url",filename)
    # print("file full url", fileurl)
    # print("template url",templateurl)
    
    directoryAdd = os.path.join(os.getcwd(), "scripts/django/media")
    file = os.path.join(directoryAdd,filename)
    
    print ("Transcribing Video: {}".format(file))
    if file.endswith(".mp4"):
        transcribe_gcs(file)
    else:
        pass
    
    # return render(request,'core/layout-vertical.html')
    context = {}
    context['segment'] = 'layout-vertical'

    html_template = loader.get_template( 'layout-vertical.html' )
    return HttpResponse(html_template.render(context, request))
