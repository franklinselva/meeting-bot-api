# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
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

@login_required(login_url="/login/")
def results(request):
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'test.txt')   #full path to text.
    data_file = open(file_path , 'r')       
    data = data_file.read()
    context = {'data': data}
    return render(request, 'core/results.html',context)

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
def simple_upload(request):
    if request.method == 'POST' and request.FILES['video']:
        myfile = request.FILES['video']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        video = os.system('python3 ../../main.py')
        
        #video= subprocess.run([sys.executable,'../../main.py'], capture_output=True, text=True, check=True)
        print(video)
        return render(request, 'core/templates/layout-vertical.html', {
            'uploaded_file_url': uploaded_file_url
        })
<<<<<<< HEAD
    return render(request, 'core/templates/layout-vertical.html')
=======
    return render(request, 'core/layout-vertical.html')


@login_required(login_url="/login/")
def external(request):
    video=request.FILES['video']
    print("video is ",video)
    fs=FileSystemStorage()
    filename=fs.save(video.name,video)
    fileurl=fs.open(filename)
    templateurl=fs.url(filename)
    print("file raw url",filename)
    print("file full url", fileurl)
    print("template url",templateurl)
    video= run([sys.executable,'../../main.py',str(fileurl),str(filename)],shell=True,stdout=PIPE)
   
    print(video.stdout)
    return render(request,'core/templates/layout-vertical.html',{'raw_url':templateurl,'edit_url':video.stdout})
>>>>>>> 4b4f7edb0f5c2bc9ce8148eb54a43788fac96133
