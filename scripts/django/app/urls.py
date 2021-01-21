# -*- encoding: utf-8 -*-
"""
MIT License
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from .views import transcribe
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', pages, name='pages'),


    # The home page
    path('', index, name='home'),
    path('simple-upload/', transcribe),
]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
