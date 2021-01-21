# -*- encoding: utf-8 -*-
"""
MIT License
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.pages, name='pages'),


    # The home page
    path('', views.index, name='home'),
<<<<<<< HEAD
    path('/simple_upload/', views.simple_upload),
]
=======
    path('external/', views.external),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 4b4f7edb0f5c2bc9ce8148eb54a43788fac96133
